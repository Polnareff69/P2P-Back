from .users import User
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid


Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    CompanyId = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name = Column(String, index=True)
    UserId = Column(UUID(as_uuid=True), ForeignKey(User.UserId))
    phonenumber = Column(String)
    description = Column(String)
    owner = relationship(User, backref="companies")
    companyimg = Column(String(255))
    companybackgrnd = Column(String(255))
    
    def to_dict(self):
        return {
            "Name": self.Name,
            "CompanyId": self.CompanyId
        }