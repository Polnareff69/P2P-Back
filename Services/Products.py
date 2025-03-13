import uuid
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.products import Product
from Repositories.GenericRepository import GenericRepository




product_repo = GenericRepository(session=conn, model=Product)
class ProductServices:
    def createProduct(product: Product):
            #new_Product = {"Name":product.Name, "Description":product.Description, "Price":product.Price, "UserId":product.UserId}
            new_product = Product(
                productid=uuid.uuid4(),  
                name=product.Name,
                description=product.Description,
                price=product.Price,
                userid=product.UserId,
                companyid = "451be262-ebe0-4f24-b41f-3c5feff5a0d6"
                )
            conn.add(new_product)
            conn.commit()
            return True
    

    def GetProduct():
          productos = product_repo.get_all()
          return productos