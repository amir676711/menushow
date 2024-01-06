from pydantic import BaseModel,Field
from typing import Union
from fastapi import FastAPI
from uuid import UUID
from typing import Union

#lat lon double
class CreateStoreRequest(BaseModel):
    faName:str
    enName:str
    address:str
    tell:str
    lat:float
    lon:float
    logoUrl:Union[str,None]=Field(default=None)
    priceUnit:str
    cityID:int
    storeType:int
    hasDelivery:bool
    hasWiFi:bool
    whatsappID:Union[str,None]=Field(default=None)
    instagramID:Union[str,None]=Field(default=None)
    telegramID:Union[str,None]=Field(default=None)

class EditStoreUser(BaseModel):
    id:int
    faName:str
    enName:str
    address:str
    tell:str
    lat:float
    lon:float
    logoUrl:Union[str,None]=Field(default=None)
    priceUnit:str
    cityID:int
    storeType:int
    hasDelivery:bool
    hasWiFi:bool
    whatsappID:Union[str,None]=Field(default=None)
    instagramID:Union[str,None]=Field(default=None)
    telegramID:Union[str,None]=Field(default=None)



