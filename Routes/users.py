from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from Utils.Auth import verify_token
from Services.Users import UsersServices


router = APIRouter(tags=["Autenticacion"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user = APIRouter()

#@user.get('/users')
#def getUsers():
#    return conn.execute(users.select()).fetchall()

#@user.post('/users')
#def createUsers(user: User):
#    UsersServices.createUser(user)
#    return JSONResponse(status_code=200, content={"message": "User created successfully"})



@user.get('/user/companies')
def Obtener_Compañias_Usuario(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid Token")
    username = payload.get("sub")
    UsersServices.getUserCompanies()
