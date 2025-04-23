from fastapi import FastAPI, Form, UploadFile, File
from pydantic import UUID4, BaseModel
from typing import Optional
from uuid import UUID
from typing import Annotated


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


class createCompanyFormData(BaseModel):
    name: Annotated[str, Form()]
    description: Annotated[str, Form()]
    phonenumber: Annotated[str, Form()]
    companyimg: Annotated[UploadFile, File()]
    companybackgrnd: Annotated[UploadFile, File()]
    
    class Config:
        orm_mode = True