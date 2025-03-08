from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from Config.db import conn
from Models.users import User as users
from Schemas.User import UserOut, UserIn, Token
from Utils.Auth import *
from Repositories.GenericRepository import GenericRepository
from Schemas.User import UserCreate
from Services.Auth import AuthServices

router = APIRouter(tags=["Autenticacion"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



# Registro de usuario
@router.post("/register")
def register_user(user: UserCreate):
    return AuthServices.RegisterUser(user)

# Login y generación del JWT
@router.post("/token", response_model=Token)
def login_for_access_token(user: UserIn):
    access_token = AuthServices.AuthenticateUser(user)
    return JSONResponse(status_code=200, content=access_token)

# Verificar usuario con JWT (ruta protegida)
@router.get("/users/me", response_model=UserOut)
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    username = payload.get("sub")
    userDB = conn.query(users).filter(users.Name == username).first()
    print(type(userDB))
    if not userDB:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.from_orm(userDB)
