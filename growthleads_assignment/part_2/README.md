# Assignment Part 2: Data Integration

This part loads csv files to a Postgres database, applies transformations such as concatenation and joining and creates the requested table.
To achieve this, the DBT (Data Build Tool) was used to load the data, apply the transformations and do field checks.

Workflow:

1. Seeding data from CSV files into the database.
2. Concatenating three tables: `legacy_data`, `tps_data`, and `sheet_stake`.
3. Merging the concatenated table with the `marketing_source` table to create a final presentation layer.


## Prerequisites

- Docker
- Docker Compose
- Python 3.x
- `pip` (Python package installer)

## Setup Instructions

### 1. Set Up PostgreSQL Database with Docker Compose

If you have successfully built the Postgres container from Part 1, skip this step. 
Otherwise: Run the docker-compose.yaml with command: `docker compose up --build -d` in order to set up the database services.

Currently the database environment has the below configuration: 

      - ports: `5434:5432`
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=analytics


## DBT Project Structure

    .
    ├── dbt_tr
    │   ├── dbt_project.yml
    │   ├── models
    │   │   ├── raw
    │   │   ├── stg
    │   │   │   └── legacy_scraper_stg.sql
    │   │   │   └── marketing_source_stg.sql
    │   │   │   └── tps_data_stg.sql
    │   │   │   └── sheet_stake_data_stg.sql
    │   │   ├── presentation
    │   │   │   └── routy_scraper_bi.sql
    │   │   └── raw__sources.yml
    │   ├── seeds
    │   │   ├── SAMPLE_marketing_source.csv
    │   │   ├── SAMPLE_postgres_legacy_scraper.csv
    │   │   ├── SAMPLE_postgres_tps_data.csv
    │   │   ├── SAMPLE_sheet_stake_data.csv
    │   └── profiles.yml


## How to run

All dbt commands are included in the python script: `run_dbt.py`, so you can just run it like:
    `python run_dbt.py` 

## Workflow Explanation

The DBT executes the below steps and in the respected order:

1. Loads the csv files aka seeds to Postgres db to schema = raw.
2. stg: Applies basic data cleaning to the data in the raw layer and stores the processed tables to the stg layer (staging).
3. presentation: Finally, it concatenates the tables from the stg layer: `legacy_scraper_stg`, `tps_data_stg`, and `sheet_stake_data_stg` and then merges the concatenated table with the table `marketing_source` in order to produce the table `routy_scraper_bi`.


### Column Mapping for concatenation
In order to concatenate the columns from the 3 tables a mapping analysis was performed. This mapping can be found in `part_2/mapping_analysis.csv`

Finally, in order to join the concatenated table with the table: `marketing_source_stg` the common field `marketing_source` was used.


## Postgres & BigQuery

DBT is used to apply data transformation using the resources of the database. It is a common practice to use Postgres for development purposes and
BigQuery when we know that our code is at it's final stages. In the file: `dbt_tr/profiles.yml` we have set the output to target either the Postgres db or the BigQuery.
In order to choose one or the other:
    `export DBT_TARGET=dev`, to target the Postgres db (development)
    `export DBT_TARGET=prod`, to target the BigQuery (production purposes)

Then run `python run_dbt.py`






