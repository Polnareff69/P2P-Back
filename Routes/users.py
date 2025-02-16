from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.users import users
from Schemas.User import User
from Services.Users import UsersServices

user = APIRouter()

@user.get('/users')
def getUsers():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def createUsers(user: User):
    UsersServices.createUser(user)
    return JSONResponse(status_code=200, content={"message": "User created successfully"})