from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
from uuid import UUID


class CreateFoodRequest(BaseModel):
   
    faName:str
    enName:str
    AmountOfFood:str
    DiscountPercent:int
    Status:bool
    CategoryID:int
    faDescription:str
    enDescription:str
    Description:str
    itemMode:str
    Title:str
    price:str

class EditFoodRequest(BaseModel):
    id:int
    faName:str
    enName:str
    AmountOfFood:str
    DiscountPercent:int
    Status:bool
    CategoryID:int
    faDescription:str
    enDescription:str
    Description:str
    itemMode:str
    Title:str
    price:str