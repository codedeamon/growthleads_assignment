# Assignment Part 1: API integration
This is the solution for the first part of the assignment which includes the following deliverables:

1. Docker Compose: Sets up a PostgreSQL service using Docker Compose.
2. API Integration: A python script that retrieves data from REST Countries endpoints, merges them and stores specific fields to the Postgres db using SQLAlchemy ORM.

## Setup and Running the script

### Prerequisites

    Docker
    Docker Compose

### 1. Set up a PostgreSQL service using Docker Compose.

Run the docker-compose.yaml with command: `docker compose up --build -d` in order to set up the database services.
It will download all necessary docker images and set up the containers.

Currently the database environment has the below configuration: 

      - ports: `5434:5432`
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=analytics

You can use any other Postgres instances, just mind to either update the database environment variables or set them in `/growthleads_assignment/part_1/settings.py`

### 2. Install Python dependencies and run the script

To install the project requirements, change to directory: `/growthleads_assignment/growthleads_assignment/part_1`
    Then run the command: `pip install -r requirements.txt`

To fetch the API data from REST Countries:
    Run: `python part1.py`


## Future Improvements

1. Improve credential configuration: Use secret management tools like Google secrets to store the credentials.
2. Improve the python script: The use of REST Countries API has space for improvement which will make the script faster.



