from pydantic import BaseModel
from uuid import UUID
from typing import Union
class UserLoginResponse(BaseModel):
    FullName:str
    tell:str
    reagentCode:str
    isAdmin:bool
    token :str

class GetUsersDetailResponed(BaseModel):
    id:UUID
    fName: str
    lName: str
    tell: str
    reagentCode:Union[str,None]
    isAdmin:bool