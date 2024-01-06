from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import uuid

class CreateprovinceRequest(BaseModel):
    # id:int
    faName: str
    enName: str

class EditprovinceRequest(BaseModel):
    faName: str
    enName: str