from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
from uuid import UUID


class CreateCityRequest(BaseModel):
    provinceID:int
    faName:str
    enName:str

class EditcityRequest(BaseModel):
    id:int
    faName: str
    enName: str