from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

user = APIRouter()

@user.get("/")
async def get_all_users():
 return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def get_user_by_id(id: int):
 return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def create_data(user: User):
 conn.execute(users.insert().values(
  name = user.name,
  age = user.age,
  message = user.message,
  createDate = user.createDate
 ))
 return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id: int, user: User):
 conn.execute(users.update().values(
  message = user.message
 ).where(users.c.id == id))
 return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
 conn.execute(users.delete().where(users.c.id == id))
 return conn.execute(users.select()).fetchall()