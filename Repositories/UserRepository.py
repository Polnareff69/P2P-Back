from sqlalchemy.orm import Session
from .GenericRepository import GenericRepository
from Models.users import User
from Models.company import Company

class UserRepository(GenericRepository):
    def __init__(self, session: Session):
        super().__init__(session, User)


    def get_user_companies(self, id):
        Companies = self.session.query(User).filter(Company.UserId == id).all()
        return Companies
