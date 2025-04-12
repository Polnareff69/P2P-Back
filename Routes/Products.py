from uuid import UUID
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Models.users import User as users
from Schemas.Products import ProductCreate 
from Services.Products import ProductServices
from fastapi import UploadFile


product = APIRouter(tags=["Productos"])

@product.post('/product/{CompanyId}')
def createProduct(product: ProductCreate, CompanyId: UUID):
    ProductServices.createProduct(product,CompanyId)
    return JSONResponse(status_code=200, content={"message": "Product created successfully"})

@product.get('/product/all')
def get_product():
    return ProductServices.GetProduct()

@product.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}