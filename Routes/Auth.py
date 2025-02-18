from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from Config.db import conn
from Models.users import users
from Schemas.User import UserOut, User, Token
from Utils.Auth import *
from sqlalchemy import select
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simulamos una base de datos (en un entorno real usarías una DB real)
fake_db = {}

# Registro de usuario
@router.post("/register")
def register_user(user: User):
    # Verificamos si el usuario ya existe
    query = select(users).where(users.c.Name == user.name)
    if conn.execute(query).fetchone():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = {"Name":user.name, "Email":user.email, "Password":hashed_password}
    conn.execute(users.insert().values(new_user))
    conn.commit()
    return JSONResponse(status_code=200, content={"message": "User created successfully"})

# Login y generación del JWT
@router.post("/token", response_model=Token)
def login_for_access_token(form_data: User):
    user = conn.get(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Crear el token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Verificar usuario con JWT (ruta protegida)
@router.get("/users/me", response_model=UserOut)
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    username = payload.get("sub")
    user = conn.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
