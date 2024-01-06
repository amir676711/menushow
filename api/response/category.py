from pydantic import BaseModel

class categoryRespones(BaseModel):
    id:int
    storeID:int
    faName:str
    enName:str