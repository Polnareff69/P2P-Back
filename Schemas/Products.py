from fastapi import FastAPI, Form, UploadFile, File
from pydantic import BaseModel
from typing import Annotated


class ProductCreate(BaseModel):
    Name: str
    Description: str
    Price: str

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    name: str


class createProductFormData(BaseModel):
    Name: Annotated[str, Form()]
    Description: Annotated[str, Form()]
    Price: Annotated[str, Form()]
    ProductImg: Annotated[UploadFile, File()]
    

    class Config:
        orm_mode = True