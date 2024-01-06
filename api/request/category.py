from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
from uuid import UUID

class createCategoryRequest(BaseModel):
    faName:str
    enName:str
    StoreID:int
    

class EditcategoryRequest(BaseModel):
    #id in  db?
    faName:str
    enName:str
    StoreID:int