from typing import Annotated

from fastapi import FastAPI, File, UploadFile




@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}




from pydantic import BaseModel
from fastapi import Form
from typing import Optional

class ProductCreate(BaseModel):
    Name: str
    Description: str
    Price: str

    class Config:
        orm_mode = True

# Función para recibir el form-data
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/create-product/")
async def create_product(
    Name: str = Form(...),
    Description: str = Form(...),
    Price: str = Form(...),
):
    product = ProductCreate(Name=Name, Description=Description, Price=Price)
    # Aquí puedes manejar el objeto `product`
    return product
