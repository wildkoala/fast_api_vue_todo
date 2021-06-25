#!/bin/bash

# Pull down latest postgres docker image

# Run the docker container
    # Name the container "test-postgres"
    # Set an env variable "POSTGRES_PASSWORD" to "mysecretpassword"
    # -d Run detached. When this scripts stops running, don't stop my container.
docker run \
--name test-postgres-db \
-e POSTGRES_PASSWORD=mysecretpassword \
-d postgres

# Log into the docker container

# Create the database

# If a flag is set, add some mock data to it