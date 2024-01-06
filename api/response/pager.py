from pydantic import BaseModel,Field
from typing import Union

class pagerRespones(BaseModel):
    id:int
    ShowPager:str
    NumberSMS:str
    RequestPager:str