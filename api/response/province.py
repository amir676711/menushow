from pydantic import BaseModel
from uuid import UUID

class provinceResponse(BaseModel):
    id:int
    faName:str
    enName:str
