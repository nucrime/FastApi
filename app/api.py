from fastapi import FastAPI

from controller import users
from controller import items
from controller import cities
from controller import text

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(cities.router)
app.include_router(text.router)
