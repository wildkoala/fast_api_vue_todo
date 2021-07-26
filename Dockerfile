# Dockerfile

# pull the official docker image
FROM python:3.9.4-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD ["uvicorn", "fast_app.main:app",  "--host", "0.0.0.0", "--port", "8000"]