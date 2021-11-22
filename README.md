# FastApi
### This example uses FastAPI - one of the fastest Python frameworks available.
#### https://fastapi.tiangolo.com/
#Prerequisites
### Install requirements
#### pip install -r requirements.txt
# Running the app
## migrate db
#### alembic init
#### alembic revision -m "init"
#### alembic upgrade head
#### alembic revision -m "users and items" --autogenerate
#### alembic upgrade head
#### or just run the following command once if you have alembic installed and versions of migrations seems to be updated 
#### alembic upgrade head
## To run use hypercorn
## https://pgjones.gitlab.io/hypercorn/
# Example
### hypercorn /controller/dispatcher.py:app --reload

### Swagger UI available at:
### http://localhost:8000/docs
