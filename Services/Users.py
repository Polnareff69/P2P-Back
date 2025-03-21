import uuid
from Config.db import conn
from Schemas.User import UserCreate
from Models.users import User
from  Repositories.GenericRepository import GenericRepository





user_repo = GenericRepository(session=conn, model=User)
class UsersServices:
    def createUser(user: UserCreate):
            #new_user = {"Name":user.name, "Email":user.email, "Password":user.password}
            new_user = User(
                UserId = uuid.uuid4(),
                Name = user.name,
                Email = user.email,
            )
            return True
    

    def getUserCompanies():
          return True