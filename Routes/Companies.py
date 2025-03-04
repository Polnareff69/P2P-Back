from fastapi import APIRouter
from Schemas.Companies import CompanyCreate
from Services.Companies import companyService
from fastapi.responses import JSONResponse


company = APIRouter()

@company.post('/company')
def Create_Company(company: CompanyCreate):
    companyService.createCompany(company)
    return JSONResponse(status_code=200, content={"message": "Company created successfully"})


@company.get('/compnay/all')
def get_companies():
    return companyService.getCompanies()