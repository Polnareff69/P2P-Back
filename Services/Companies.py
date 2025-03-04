import uuid
from Config.db import conn
from Models.company import Company
from Repositories.GenericRepository import GenericRepository


product_repo = GenericRepository(session=conn, model=Company)

class companyService:
    def createCompany(company: Company):
        new_company = Company(
            Name = company.name,
            UserId = company.userid
        )
        product_repo.create(new_company)
        return True