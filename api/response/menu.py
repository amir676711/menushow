from pydantic import BaseModel,Field
from typing import Union

class menuRespones(BaseModel):
    ResturantName:str
    LogoUrl:str
    BackgroundPicture:str
    graphicUrl:str
    PhoneNumber:Union[int,None]=Field(default=None)
    Address:str