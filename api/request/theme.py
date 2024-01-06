from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
from uuid import UUID
from datetime import datetime

class createThemeRequest(BaseModel):
    Name : str
    ThemeUrl:str
    Price:str
    

class EditThemeRequest(BaseModel):
    id:int
    Name : str
    ThemeUrl:str