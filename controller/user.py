from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

LAST_ITEM = -1

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None


db = []


@app.post("/users/")
async def create_user(user: User):
    db.append(user.dict())
    return db[LAST_ITEM]


@app.get("/users/")
async def get_users():
    return db


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return db[user_id - 1]


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return db.pop(user_id - 1)

