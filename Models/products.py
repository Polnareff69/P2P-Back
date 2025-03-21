from .users import User
from .company import Company
from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    productid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(String(255))
    companyid = Column(UUID(as_uuid=True), ForeignKey(Company.CompanyId))
    company = relationship(Company, backref="products")

    # Método to_dict para convertir a diccionario
    def to_dict(self):
        return {
            "Name": self.Name,
            "Description": self.Description,
            "Price": self.Price,
            
        }
