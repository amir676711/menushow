from pydantic import BaseModel,Field
from uuid import UUID
from typing import Union

class storeRespones(BaseModel):
    id:int
    faName:str
    enName:str
    address:str
    tell:str
    lat:float
    lon:float
    logoUrl:Union[str,None]=Field(default=None)
    priceUnit:str
    cityID:Union[int,None]=Field(default=None)
    storeType:Union[int,None]=Field(default=None)
    hasDelivery:bool
    hasWiFi:bool
    whatsappID:Union[str,None]=Field(default=None)
    instagramID:Union[str,None]=Field(default=None)
    telegramID:Union[str,None]=Field(default=None)

