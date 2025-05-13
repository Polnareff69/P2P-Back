import uuid
from Config.db import conn
from Models.company import Company
from Models.products import Product
from Models.users import User
from Schemas.Companies import UpdateCompany, createCompanyFormData
from Repositories.GenericRepository import GenericRepository
from Repositories.ProductRepository import ProductRepository
import os


company_repo = GenericRepository(session=conn, model=Company)
user_repo = GenericRepository(session=conn, model=User)
product_repo = ProductRepository(session=conn)

class companyService:
    
    def createCompanyWithUser(company: Company, userName: str):
        user = user_repo.get_by_name("Name", userName)
        new_company = Company(
            CompanyId = uuid.uuid4(),
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
        products = product_repo.getCompanyProducts(id)
        products = [product for product in products]
        return products
    
    def getOwner(id: uuid):
        company = company_repo.get_by_id("CompanyId", id)
        user = company.owner
        return user
    
    async def createCompanyWithUserImg(company: createCompanyFormData, userName: str):
        user = user_repo.get_by_name("Name", userName)
        companyImg = company.companyimg
        file_location1 = os.path.join("/home/ubuntu/P2P-Back-NAS", companyImg.filename)
        companybackgrnd = company.companybackgrnd
        file_location2 = os.path.join("/home/ubuntu/P2P-Back-NAS", companybackgrnd.filename)
        new_company = Company(
            CompanyId = uuid.uuid4(),
            Name = company.name,
            UserId = user.UserId,
            phonenumber = company.phonenumber,
            description = company.description,
            companyimg = file_location1,
            companybackgrnd = file_location2
        )
        nuevo_rol = {
            "Role":"seller"
        }
        user_repo.update("UserId", user.UserId, nuevo_rol)
        company_repo.create(new_company)
        with open(file_location1, "wb") as f:
            content = await companyImg.read()
            f.write(content)
        with open(file_location2, "wb") as f:
            content = await companybackgrnd.read()
            f.write(content)

        return new_company
    

    def getCompanyById(company_id: uuid.UUID):
        company = company_repo.get_by_id_relation("CompanyId", company_id, relationships=["owner"])
        if not company:
            raise ValueError(f"No se encontró una compañía con ID: {company_id}")
        return company
