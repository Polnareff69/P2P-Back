import uuid
from Config.db import conn
from Models.company import Company
from Repositories.GenericRepository import GenericRepository


company_repo = GenericRepository(session=conn, model=Company)

class companyService:
    def createCompany(company: Company):
        new_company = Company(
            Name = company.name,
            UserId = company.userid,
            phonenumber = company.phonenumber,
            description = company.description
        )
        company_repo.create(new_company)
        return True
    

    def getCompanies():
        companies = company_repo.get_all()
        return companies