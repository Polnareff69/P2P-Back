import uuid
from fastapi.responses import JSONResponse
from Config.db import conn
from Models.products import Product





class ProductServices:
    def createProduct(product: Product):
            #new_Product = {"Name":product.Name, "Description":product.Description, "Price":product.Price, "UserId":product.UserId}
            new_product = Product(
                productid=uuid.uuid4(),  # Generamos un UUID para ProductId
                name=product.Name,
                description=product.Description,
                price=product.Price,
                userid=product.UserId)
            conn.add(new_product)
            conn.commit()
            return True