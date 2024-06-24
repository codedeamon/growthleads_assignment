from setuptools import setup, find_packages

setup(
    name="assignment",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sqlalchemy",
        "python-restcountries",
        "psycopg2"
    ],
    extras_requires={
        'dev': [
            'pip-tools',
        ],
    },
    python_requires='>=3.8',
)

