from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Session
from database import models
from uuid import UUID
from datetime import datetime


def create_ticket(db: Session, creator: UUID,text:str,subject:str):
    newTicket = models.Ticket(
        subject=subject, creator=creator, startDate=datetime.now(),crateAt=datetime.now(), text=text
    )
    db.add(newTicket)
    db.commit()
    db.refresh(newTicket)
    return newTicket

def get_tickets(db: Session):
    return db.query(models.Ticket).all()


def create_ticket_meesage(db: Session, ticketID: int, creator: UUID, text: str):
    newMessage = models.TrackMessage(
        accountID=creator, text=text, createdAt=datetime.now(), ticketID=ticketID
    )
    db.add(newMessage)
    db.commit()
    db.refresh(newMessage)
    return newMessage


# ? ? ? ? ?
def get_ticket_message(db: Session, messageID: int):
    return (
        db.query(models.TicketMessage)
        .filter(models.TicketMessage.id == messageID)
        .first()
    )



