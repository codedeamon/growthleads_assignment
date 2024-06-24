import os

# db credentials
POSTGRES_USER = os.getenv('POSTGRES_USER','postgres')
POSTGRES_PASS = os.getenv('POSTGRES_PASS','postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT','5434')
POSTGRES_HOST = os.getenv('POSTGRES_HOST','localhost')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'analytics')


########### part 1 ############

# used to retrieve info for these countries
country_names = {"France", "Greece", "Turkey"}

# used these currencies to get info on countries that use them
currencies = ['usd', 'eur']

# used subregions to retrieve country names that belong at those subregions
subregions = ['Northern Europe', 'Northern America', 'Eastern Africa']

# country data fields list
data_filter_list = ['name',
                    'borders',
                    'region',
                    'currencies',
                    'subregion',
                    'population',
                    'capital']