from sqlalchemy import Column, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.ext.declarative import declarative_base # o ajusta según tu estructura
from .users import User
from .products import Product  # asegúrate de que este archivo/modelo exista


Base = declarative_base()


class Auction(Base):
    __tablename__ = 'auctions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey(Product.productid), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey(User.UserId), nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    initial_price = Column(Integer, nullable=False)
    current_price = Column(Integer)

    product = relationship(Product, backref="auctions")
    owner = relationship(User, backref="owned_auctions")

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "owner_id": self.owner_id,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "initial_price": self.initial_price,
            "current_price": self.current_price
        }
