from fastapi import FastAPI

from controller import users
from controller import items

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
