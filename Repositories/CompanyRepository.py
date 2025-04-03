from sqlalchemy.orm import Session
from .GenericRepository import GenericRepository
from Models.company import Company

class ProductRepository(GenericRepository):
    def __init__(self, session: Session):
        super().__init__(session, Company)


    def getCompanyProducts(self, id):
        productos = self.session.query(Company).filter(Company.companyid == id).all()
        return productos
