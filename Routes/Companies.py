from uuid import UUID
from fastapi import APIRouter, HTTPException ,Depends
from fastapi.security import OAuth2PasswordBearer
from Schemas.Companies import CompanyCreateNoUser, createCompanyFormData, UpdateCompany, CompanyOut, CompanyFullOut
from Schemas.Products import ProductOut
from Schemas.User import UserOut
from Services.Companies import companyService
from fastapi.responses import JSONResponse
from Utils.Auth import verify_token


company = APIRouter(tags=["Compañias"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@company.get('/compnay/all')
def get_companies():
    return companyService.getCompanies()

@company.post('/companyOld')
def Create_Company(company: CompanyCreateNoUser,token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    userName = payload.get("sub")
    compani = companyService.createCompanyWithUser(company,userName)
    company_instance = CompanyOut.model_validate(compani)
    company_dict = company_instance.model_dump()
    company_dict['CompanyId'] = str(company_dict['CompanyId']) 
    return JSONResponse(status_code= 200, content={"Message":"Puro sexo", "Company":company_dict})


@company.put('/company/update')
def Update_Company(company: UpdateCompany):
    companyService.updateCompanies(company)
    return JSONResponse(status_code=200, content="Empresa Actualizada mi papa")


@company.delete('/company/{CompanyId}')
def Delete_Company(CompanyId: UUID):
    companyService.deleteCompanies(CompanyId)
    return JSONResponse(status_code=200, content="Company delete Sucessfull") 


@company.get('/company/products/{CompanyId}', response_model=list[ProductOut])
def Get_Company_Products(CompanyId: UUID):
    return companyService.getProducsFromCompany(CompanyId)


@company.get('/company/owner/{CompanyId}', response_model=UserOut)
def get_Company_Owner(CompanyId: UUID):
    return companyService.getOwner(CompanyId)


@company.post('/company')
async def Create_CompanyImg(company: createCompanyFormData  = Depends(), token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    userName = payload.get("sub")
    compani = await companyService.createCompanyWithUserImg(company,userName)
    company_instance = CompanyOut.model_validate(compani)
    company_dict = company_instance.model_dump()
    company_dict['CompanyId'] = str(company_dict['CompanyId']) 
    return JSONResponse(status_code= 200, content={"Message":"Puro sexo", "Company":company_dict})

@company.get('/company/{CompanyId}', response_model=CompanyFullOut)
def Get_Company_By_Id(CompanyId: UUID):
    company = companyService.getCompanyById(CompanyId)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return CompanyFullOut.model_validate(company)


