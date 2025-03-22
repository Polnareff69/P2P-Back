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
          def getUserCompanies(userName: str):
                user = user_repo.get_by_name("Name", userName)
                userid = user.id
                companies = user_repo.get_related()
