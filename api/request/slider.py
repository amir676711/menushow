from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import uuid

class CreateSliderRequest(BaseModel):
    # id:int
    Picture: str
    Number: int

class EditSliderRequest(BaseModel):
    Picture: str
    Number: int