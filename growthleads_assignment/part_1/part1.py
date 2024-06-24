'''

A Python script that fetches data from 3 different endpoints in a sample third-party API and stores it to a Postgres database.

'''

import requests
import logging

from growthleads_assignment.utils import insert_data_to_db
from growthleads_assignment.part_1.models import *
from growthleads_assignment.settings import *

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from restcountries import RestCountryApiV2 as rapi



# Fetch data from APIs
def fetch_data(endpoint: str, query: str) -> Optional[dict]:
    url = endpoint.format(query)
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[0]  # Assuming the first item is what we need
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logger.error(f"Other error occurred: {err}")
    return None


# Main function
def main():
    # api_endpoints = {
    #     'name': 'https://restcountries.com/v3.1/name/{}?fullText=true',
    #     'capital': 'https://restcountries.com/v3.1/capital/{}',
    #     'currency': 'https://restcountries.com/v3.1/currency/{}'
    # }

    country_data_list = []

    country_names = {"France", "Greece", "Turkey"}



    currencies = ['usd', 'eur']

    for currency in currencies:

        try:
            # endpoint 2: fetch by currency
            countries_fetched = rapi.get_countries_by_currency(currency=currency, filters=data_filter_list)
            for country in countries_fetched:
                country_names.add(country.name)

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}, currency = {currency}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}, currency = {currency}")
            return None




    subregions = ['Northern Europe', 'Northern America', 'Eastern Africa']

    for subregion in subregions:
        # endpoint 3: fetch by subregion
        try:
            countries_fetched = rapi.get_countries_by_subregion(subregion=subregion, filters=data_filter_list)
            for country in countries_fetched:
                country_names.add(country.name)
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}, subregion = {subregion}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}, subregion = {subregion}")
            return None


    counter = 0
    for country in country_names:

        counter += 1
        # get first 5 countries
        if counter > 2:
            break

        try:
            # endpoint 1: fetch by country name
            country = rapi.get_countries_by_name(name=country)[0]
            country_data_list.append(
                CountryModel(
                    name=country.name,
                    capital=country.capital,
                    region=country.region,
                    subregion=country.subregion,
                    population=country.population,
                    currency=country.currencies[0]['code']))
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}, country = {country}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}, country = {country}")
            return None


    # Insert data
    insert_data_to_db(country_data_list)


if __name__ == "__main__":
    main()


