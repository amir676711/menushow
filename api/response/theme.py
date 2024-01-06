from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import uuid

class CreateThemeRespones(BaseModel):
    id:int
    Name: str
    ThemeUrl: str
    Price:str