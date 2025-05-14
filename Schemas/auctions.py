# Schemas/auction.py

from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
from Schemas.User import UserOut  # Asegúrate de tener este schema
from Schemas.Products import ProductOut  # Este deberías crearlo también

class AuctionCreate(BaseModel):
    product_id: UUID4
    owner_id: UUID4
    start_date: datetime
    end_date: datetime
    initial_price: int
    current_price: Optional[int] = None

    class Config:
        orm_mode = True


class AuctionUpdate(BaseModel):
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    current_price: Optional[int]

    class Config:
        orm_mode = True


class AuctionOut(BaseModel):
    id: UUID4
    product_id: UUID4
    owner_id: UUID4
    start_date: datetime
    end_date: datetime
    initial_price: int
    current_price: Optional[int]

    class Config:
        from_attributes = True
        orm_mode = True


class AuctionFullOut(AuctionOut):
    owner: Optional[UserOut]
    product: Optional[ProductOut]

    class Config:
        from_attributes = True
        orm_mode = True
