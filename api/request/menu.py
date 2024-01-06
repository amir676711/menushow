from pydantic import BaseModel,Field
from typing import Union
from fastapi import FastAPI




class CreateMenuRequest(BaseModel):
    ResturantName:str
    LogoUrl:str
    BackgroundPicture:str
    graphicUrl:str
    PhoneNumber:Union[int,None]=Field(default=None)
    Address:str

class EditMenuRequest(BaseModel):
    id:int
    ResturantName:str
    LogoUrl:str
    BackgroundPicture:str
    graphicUrl:str
    PhoneNumber:Union[int,None]=Field(default=None)
    Address:str