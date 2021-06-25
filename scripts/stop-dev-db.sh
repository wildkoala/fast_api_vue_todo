#!/bin/bash

# Get the container we're using for the dev-db
to_stop=$(docker ps --filter "name=test-postgres-db" -q)

# Stop the dev db
to_rm=$(docker stop $to_stop)

# Delete the container
docker rm $to_rm
