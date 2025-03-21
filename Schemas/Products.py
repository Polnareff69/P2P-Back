from fastapi import FastAPI
from pydantic import UUID4, BaseModel


class ProductCreate(BaseModel):
    Name: str
    Description: str
    Price: str

    class Config:
        orm_mode = True