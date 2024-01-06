from pydantic import BaseModel,Field
from typing import Union
from fastapi import FastAPI




class CreatePagerRequest(BaseModel):
    ShowPager:str
    NumberSMS:str
    RequestPager:str

class EditPagerRequest(BaseModel):
    id:int
    ShowPager:str
    NumberSMS:str
    RequestPager:str