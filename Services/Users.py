import uuid
from Config.db import conn
from Schemas.User import UserCreate
from Models.users import User
from  Repositories.GenericRepository import GenericRepository
from Repositories.UserRepository import UserRepository
from Repositories.CompanyRepository import CompanyRepository



user_repository = UserRepository(session=conn)
company_repository = CompanyRepository(session=conn)
class UserServices:
    def createUser(user: UserCreate):
            #new_user = {"Name":user.name, "Email":user.email, "Password":user.password}
            new_user = User(
                UserId = uuid.uuid4(),
                Name = user.name,
                Email = user.email,
            )
            return True
    

    def getUserCompanies(username : str):
          user = user_repository.get_by_name("Name",username)
          companies = company_repository.getUserCompnay(user.UserId)
          companies = [company for company in companies]
          return companies
          