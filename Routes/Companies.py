from fastapi import APIRouter, HTTPException ,Depends
from fastapi.security import OAuth2PasswordBearer
from Schemas.Companies import CompanyCreateNoUser, CompanyCreate
from Services.Companies import companyService
from fastapi.responses import JSONResponse
from Utils.Auth import verify_token


company = APIRouter(tags=["Compañias"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@company.post('/company')
def Create_Company(company: CompanyCreate):
    companyService.createCompany(company)
    return JSONResponse(status_code=200, content={"message": "Company created successfully"})


@company.get('/compnay/all')
def get_companies():
    return companyService.getCompanies()

@company.post('/company/user')
def Create_Company_User(company: CompanyCreateNoUser,token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    userName = payload.get("sub")
    print(userName)
    companyService.createCompanyWithUser(company,userName)
    return JSONResponse(status_code= 200, content="Puro sexo")