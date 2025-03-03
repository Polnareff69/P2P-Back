from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from Config.db import conn
from Models.users import User as users
from Schemas.User import UserOut, User, Token
from Utils.Auth import *
from sqlalchemy import select
from Repositories.GenericRepository import GenericRepository
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



# Registro de usuario
@router.post("/register")
def register_user(user: User):
    # Verificamos si el usuario ya existe
    query = select(users).where(users.Name == user.name)
    if conn.execute(query).fetchone():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = users(
        Name = user.name,
        Email= user.email,
        Password = hashed_password, 
        Role = "user"
    )
    conn.add(new_user)
    conn.commit()
    return JSONResponse(status_code=200, content={"message": "User created successfully"})

# Login y generación del JWT
@router.post("/token", response_model=Token)
def login_for_access_token(user: User):
    userDB = conn.query(users).filter(users.Name == user.name).first()
    print(type(userDB))
    if not userDB or not verify_password(user.password, userDB.Password):
        return JSONResponse(status_code=401, content={"message": "Papi por aqui no es"})
    access_token = create_access_token(data={"sub": user.name, "email":user.email, "Role":user.role})
    return JSONResponse(status_code=200, content={"access_token": access_token, "token_type": "bearer"})

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
