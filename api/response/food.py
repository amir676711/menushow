from pydantic import BaseModel

class foodRespones(BaseModel):
    id:int
    faName:str
    enName:str
    AmountOfFood:str
    DiscountPercent:int
    Status:bool
    CategoryID:int
    faDescription:str
    enDescription:str
    Description:str
    itemMode:str
    Title:str
    price:str