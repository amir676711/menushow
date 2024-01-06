from pydantic import BaseModel

class cityRespones(BaseModel):
    id:int
    provinceID:int
    faName:str
    enName:str