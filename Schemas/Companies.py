from fastapi import FastAPI
from pydantic import UUID4, BaseModel


class CompanyCreate(BaseModel):
    name: str
    userid: UUID4

    class Config:
        orm_mode = True 