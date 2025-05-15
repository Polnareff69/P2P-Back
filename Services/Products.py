import uuid
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.products import Product
from Models.users import User
from Models.company import Company
from Repositories.GenericRepository import GenericRepository
from Schemas.Products import createProductFormData
import os



product_repo = GenericRepository(session=conn, model=Product)
user_repo = GenericRepository(session=conn, model=User)
company_repo = GenericRepository(session=conn, model=Company)
class ProductServices:
    def createProduct(product: Product, companyId: str):
            company = company_repo.get_by_id("CompanyId", companyId)
            if not company:
                  id = uuid.uuid4()
            id = company.CompanyId
            new_product = Product(
                productid=uuid.uuid4(),  
                name=product.Name,
                description=product.Description,
                price=int(product.Price),
                companyid = id
                )
            product_repo.create(new_product)
            return JSONResponse(status_code=200, content={"message": "Product created successfully"})
    
    async def createProductImg(product: createProductFormData, companyId: str):
        company = company_repo.get_by_id("CompanyId", companyId)
        if not company:
                id = uuid.uuid4()
        else: 
              id = company.CompanyId
        file = product.ProductImg
        file_location = os.path.join("/home/ubuntu/P2P-Back-NAS", file.filename)
        new_product = Product(
            productid=uuid.uuid4(),  
            name=product.Name,
            description=product.Description,
            price=int(product.Price),
            companyid = id,
            productimg = file_location
            )
        product_repo.create(new_product)
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)
        return JSONResponse(status_code=200, content={"message": "Product created successfully", "Nombre": product.Name, "Price": product.Price ,"saved_to": file_location})

    

    def GetProduct():
          productos = product_repo.get_all()
          return productos
    
    async def GetProductImg(fileLocation: str):
          return fileLocation