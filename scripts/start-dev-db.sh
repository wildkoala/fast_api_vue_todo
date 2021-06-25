#!/bin/bash


# Name the container "test-postgres"
# Set a couple env variables used by postgres
# -d Run detached. When this scripts stops running, don't stop my container.
# Let's make port 5432 map to port 5432 on my host machine.
# The image I want is postgres. I'm not specifying a version, so docker will
# just get the lastest version
docker run \
    --detach \
    --rm \
    --name test-postgres-db \
    --env POSTGRES_USER=wildkoala \
    --env POSTGRES_PASSWORD=also_wildkoala \
    --env POSTGRES_DB=fast_api_vue_db \
    --publish '5432:5432' \
    postgres

# Log into the docker container
# Execute this command on the docker container.
# Give me an interactive prompt on the test-postgres-db container
# Use the postgres client command psql to log in and connect to our test database
docker container exec \
    -it test-postgres-db \
    psql -U wildkoala fast_api_vue_db

# Create the database

# If a flag is set, add some mock data to it