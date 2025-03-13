from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Models.users import User as users
from Schemas.Products import ProductCreate 
from Services.Products import ProductServices


product = APIRouter(tags=["Productos"])

@product.post('/product')
def createProduct(product: ProductCreate):
    ProductServices.createProduct(product)
    return JSONResponse(status_code=200, content={"message": "User created successfully"})

@product.get('/product/all')
def get_product():
    return ProductServices.GetProduct()