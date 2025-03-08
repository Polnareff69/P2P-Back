from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from Schemas.User import UserCreate
from Models.users import User 
from Repositories.GenericRepository import GenericRepository
from Config.db import conn
from Utils.Auth import get_password_hash


user_repo = GenericRepository(session=conn, model=User)
class AuthServices:
    def RegisterUser(user: UserCreate):
        Usuario = user_repo.get_by_name("Name", user.name)
        if Usuario:
            raise HTTPException(status_code=400, detail="Username already registered")
    
        hashed_password = get_password_hash(user.password)
        new_user = User(
            Name=user.name,
            Email=user.email,
            Password=hashed_password,
            Role="user"
        )
        user_repo.create(new_user)
        return JSONResponse(status_code=200, content={"message": "User created successfully"})

