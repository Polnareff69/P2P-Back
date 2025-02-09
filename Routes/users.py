from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.users import users
from Schemas.User import User

user = APIRouter()

@user.get('/users')
def getUsers():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def createUsers(user: User):
    new_user = {"Name":user.name, "Email":user.email, "Password":user.password}
    conn.execute(users.insert().values(new_user))
    conn.commit()
    return JSONResponse(status_code=200, content={"message": "User created successfully"})