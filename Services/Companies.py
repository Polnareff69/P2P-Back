import uuid
from Config.db import conn
from Models.company import Company
from Models.products import Product
from Models.users import User
from Schemas.Companies import UpdateCompany 
from Repositories.GenericRepository import GenericRepository


company_repo = GenericRepository(session=conn, model=Company)
user_repo = GenericRepository(session=conn, model=User)
product_repo = GenericRepository(session=conn, model=Product)

class companyService:
    
    def createCompanyWithUser(company: Company, userName: str):
        user = user_repo.get_by_name("Name", userName)
        new_company = Company(
            Name = company.name,
            UserId = user.UserId,
            phonenumber = company.phonenumber,
            description = company.description,
        )
        nuevo_rol = {
            "Role":"seller"
        }
        user_repo.update("UserId", user.UserId, nuevo_rol)
        company_repo.create(new_company)
        return new_company
    
    def getCompanies():
        companies = company_repo.get_all()
        return companies
    
    def updateCompanies(company: UpdateCompany):
        companyUpdate = company_repo.updateByName("Name", company.name, company.dict(exclude_unset=True))
        return True

    def deleteCompanies(id : uuid):
        company_repo.delete("CompanyId",id)
        return True
    
    def getProducsFromCompany(id: uuid):
        company = company_repo.get_by_id("CompanyId", id)
        products = company_repo.get_related(Product)
        # Accediendo solo a los productos
        products = [product for product, _ in products]
        return products