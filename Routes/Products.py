from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from Models.users import User as users
from Schemas.Products import ProductCreate, createProductFormData
from Services.Products import ProductServices
from fastapi import UploadFile
import os
from fastapi.responses import FileResponse


product = APIRouter(tags=["Productos"])

@product.post('/productOld/{CompanyId}')
def createProduct(product: ProductCreate, CompanyId: UUID):
    ProductServices.createProduct(product,CompanyId)
    return JSONResponse(status_code=200, content={"message": "Product created successfully"})

@product.get('/product/all')
def get_product():
    return ProductServices.GetProduct()

@product.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@product.post('/product/{CompanyId}')
async def create_upload_file_save(CompanyId: UUID, product_form_data: createProductFormData = Depends()):
    producto = await ProductServices.createProductImg(product_form_data, CompanyId)
    return producto

@product.get("/ProductImg",response_class=FileResponse)
async def getProductImg(fileLocation:str):
    return fileLocation