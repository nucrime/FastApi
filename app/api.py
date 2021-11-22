from fastapi import FastAPI

from controller import users
from controller import items
from controller import root

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(root.router)
