from fastapi import FastAPI
from pydantic import UUID4, BaseModel
from typing import Optional
from uuid import UUID


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
        
class UpdateCompany(BaseModel):
    name: str
    phonenumber: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class CompanyOut(BaseModel):
    CompanyId: UUID
    Name: str

    class Config:
        from_attributes=True
        orm_mode = True