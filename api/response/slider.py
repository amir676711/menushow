from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
import uuid

class CreateSliderRespones(BaseModel):
    id:int
    Picture: str
    Number: int