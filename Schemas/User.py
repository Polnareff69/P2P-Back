from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str


class UserOut(BaseModel):
    Name: str
    Email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str