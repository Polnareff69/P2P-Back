from fastapi import FastAPI
from pydantic import UUID4, BaseModel


class CompanyCreate(BaseModel):
    name: str
    phonenumber: str 
    description: str
    userid: UUID4

    class Config:
        orm_mode = True 

class CompanyCreateNoUser(BaseModel):
    name: str
    phonenumber: str 
    description: str

    class Config:
        orm_mode = True 