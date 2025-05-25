# Schemas/university.py

from pydantic import BaseModel, UUID4
from typing import Optional


class UniversityCreate(BaseModel):
    name: str
    address: str

    class Config:
        orm_mode = True


class UniversityUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True


class UniversityOut(BaseModel):
    id: UUID4
    name: str
    address: str

    class Config:
        from_attributes = True  # Para compatibilidad con SQLAlchemy
        orm_mode = True
