from sqlalchemy.orm import Session
from .GenericRepository import GenericRepository
from Models.company import Company

class CompanyRepository(GenericRepository):
    def __init__(self, session: Session):
        super().__init__(session, Company)


    def getUserCompnay(self, id):
        companies = self.session.query(Company).filter(Company.UserId == id).all()
        return companies
