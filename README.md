# FastAPI + Vue template app to get on the BDP for testing.

## App Design
- The data is stored in a postgres database. I'm going to mock this locally with a postgres database in a docker container.
- I'm using FastAPI to create endpoints that take requests, do security checks with the BDP and query the database.
- I'm using Vue to make calls for the data each screen will need and make a nice UI that doesn't have to reload the whole page every time I get new data.

## Running the app locally
uvicorn main:app --reload

