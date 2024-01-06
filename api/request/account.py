from pydantic import BaseModel,Field
from typing import Union
from fastapi import FastAPI
from uuid import UUID
from typing import Union

class CreateUserRequest(BaseModel):
    fName :str
    lName :str
    password :str
    tell: str
    reagentCode:Union[str,None]=Field(default=None)
    isAdmin:bool

class LoginUserRequest(BaseModel):
    tell: str
    password: str

class EditUserRequst(BaseModel):
    id :UUID
    fName :str
    lName :str
    tell: str
 
class EditUSerByAdmin(BaseModel):
    fName :str
    lName :str
    password :str
    tell: str
    reagentCode:Union[UUID,None]=Field(default=None)
    isAdmin:bool

class UserPasswordChangeRequest(BaseModel):
    id:UUID
    password:str

