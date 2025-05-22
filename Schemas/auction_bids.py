# Schemas/auction_bid.py

from pydantic import BaseModel, UUID4
from typing import Optional
from Schemas.User import UserOut
from Schemas.auctions import AuctionOut


class AuctionBidCreate(BaseModel):
    auction_id: UUID4
    user_id: UUID4
    bid_amount: int

    class Config:
        orm_mode = True


class AuctionBidOut(BaseModel):
    id: UUID4
    auction_id: UUID4
    user_id: UUID4
    bid_amount: int
    user: Optional[UserOut]

    class Config:
        from_attributes = True
        orm_mode = True


class AuctionBidFullOut(AuctionBidOut):
    user: Optional[UserOut]
    auction: Optional[AuctionOut]

    class Config:
        from_attributes = True
        orm_mode = True
