from Config.db import conn
from Schemas.User import User
from Models.users import users





class UsersServices:

    def createUser(user: User):
            new_user = {"Name":user.name, "Email":user.email, "Password":user.password}
            conn.execute(users.insert().values(new_user))
            conn.commit()
            return True