from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    UserId = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name = Column(String(255))
    Email = Column(String(255))
    Password = Column(String(255))

    

    # Método to_dict para convertir a diccionario
    def to_dict(self):
        return {
            "UserId": str(self.UserId),
            "Name": self.Name,
            "Email": self.Email,
            "Password": self.Password
        }
