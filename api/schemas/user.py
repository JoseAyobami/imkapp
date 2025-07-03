from pydantic import BaseModel, EmailStr
from typing import Optional


class ORMBase(BaseModel):
    from_attribute = True

class UserRecord(ORMBase):
    username: str
    email: EmailStr
    password: str
    bio: str

class UserCreate(UserRecord):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class Users(UserRecord):
    id: int
    is_active: bool = True


class User(BaseModel):
    username: str
    password: str    

# class ShowUser(ORMBase):
#     username: str
#     email: EmailStr 
#     # blogs: list["BlogRecord"] = []    

