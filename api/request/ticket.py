from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CreateTicketRequest(BaseModel):
    subject : str
    text: str

class EditTicketRequest(BaseModel):
    id:int #ID of ticekt
    subject: str
    text:str
class CreateTicketMessegeRequest(BaseModel):
    Text: str
    ticketID : int

class EditTicketkMessage(BaseModel):
    id :int # ID of TrackMessage
    text : str

class LockTicketRequest(BaseModel):
    ticketID:int
    locked:bool
