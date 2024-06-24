import os

# db credentials
POSTGRES_USER = os.getenv('POSTGRES_USER','postgres')
POSTGRES_PASS = os.getenv('POSTGRES_PASS','postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT','5434')
POSTGRES_HOST = os.getenv('POSTGRES_HOST','localhost')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'analytics')


# country data fields list
data_filter_list = ['name',
                    'borders',
                    'region',
                    'currencies',
                    'subregion',
                    'population',
                    'capital']