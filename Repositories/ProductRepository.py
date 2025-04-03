from sqlalchemy.orm import Session
from .GenericRepository import GenericRepository
from Models.products import Product

class ProductRepository(GenericRepository):
    def __init__(self, session: Session):
        super().__init__(session, Product)


    def getCompanyProducts(self, id):
        productos = self.session.query(Product).filter(Product.companyid == id).all()
        return productos
