from fastapi import APIRouter, HTTPException ,Depends
from fastapi.security import OAuth2PasswordBearer
from Schemas.Companies import CompanyCreateNoUser, CompanyCreate, UpdateCompany
from Services.Companies import companyService
from fastapi.responses import JSONResponse
from Utils.Auth import verify_token


company = APIRouter(tags=["Compañias"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@company.get('/compnay/all')
def get_companies():
    return companyService.getCompanies()

@company.post('/company')
def Create_Company(company: CompanyCreateNoUser,token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    userName = payload.get("sub")
    print(userName)
    companyService.createCompanyWithUser(company,userName)
    return JSONResponse(status_code= 200, content="Puro sexo")


@company.post('/company/update')
def Update_Company(company: UpdateCompany):
    companyService.updateCompanies(company)
    return JSONResponse(status_code=200, content="Empresa Actualizada mi papa")