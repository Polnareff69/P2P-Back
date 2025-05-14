from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from sqlalchemy.ext.declarative import declarative_base
from .users import User
from .auction import Auction

Base = declarative_base()

class AuctionBid(Base):
    __tablename__ = 'auction_bids'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auction_id = Column(UUID(as_uuid=True), ForeignKey(Auction.id), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.UserId), nullable=False)
    bid_amount = Column(Integer)

    auction = relationship(Auction, backref="bids")
    user = relationship(User, backref="bids")

    def to_dict(self):
        return {
            "id": self.id,
            "auction_id": self.auction_id,
            "user_id": self.user_id,
            "bid_amount": self.bid_amount
        }
