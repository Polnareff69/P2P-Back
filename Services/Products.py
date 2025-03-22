import uuid
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.products import Product
from Models.users import User
from Models.company import Company
from Repositories.GenericRepository import GenericRepository




product_repo = GenericRepository(session=conn, model=Product)
user_repo = GenericRepository(session=conn, model=User)
company_repo = GenericRepository(session=conn, model=Company)
class ProductServices:
    def createProduct(product: Product, companyId: str):
            company = company_repo.get_by_id("CompanyId", companyId)
            if not company:
                  return False
            new_product = Product(
                productid=uuid.uuid4(),  
                name=product.Name,
                description=product.Description,
                price=int(product.Price),
                companyid = company.CompanyId
                )
            product_repo.create(new_product)
            return JSONResponse(status_code=200, content={"message": "Product created successfully"})

    

    def GetProduct():
          productos = product_repo.get_all()
          return productos