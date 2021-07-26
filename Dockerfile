FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./fast_app /fast_app
CMD ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "8000"]