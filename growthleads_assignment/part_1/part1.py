'''

Part 1: A Python script that fetches data from 3 different endpoints in a sample third-party API and stores it to a Postgres database.

'''

import requests
import logging
from utils import insert_data_to_db
from models import *
from settings import *

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from restcountries import RestCountryApiV2 as rapi


def main():

    country_data_list = []
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

    for country in country_names:
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


