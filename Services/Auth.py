from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from Schemas.User import UserCreate, UserIn
from Models.users import User 
from Repositories.GenericRepository import GenericRepository
from Config.db import conn
from Utils.Auth import create_access_token, get_password_hash, verify_password


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
        acces_token = create_access_token(data={"sub": user.name, "email": user.email, "Role": "user"})
        return JSONResponse(status_code=200, content={"message": "User created successfully", "Token": acces_token})

    def AuthenticateUser(user: UserIn):
        Usuario = user_repo.get_by_name("Name", user.name)
        
        if not Usuario or not verify_password(user.password, Usuario.Password):
            raise HTTPException(status_code=401, detail="Papi, por aquí no es")

        access_token = create_access_token(data={"sub": Usuario.Name, "email": Usuario.Email, "Role": Usuario.Role})
        return {"access_token": access_token, "token_type": "bearer"}