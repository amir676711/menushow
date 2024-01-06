from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from sqlalchemy.orm import Session
import services.jwt as jwt
from database.CRUD import ticket
from api.request.ticket import CreateTicketRequest,EditTicketRequest,CreateTicketMessegeRequest,EditTicketkMessage
from api.responses.ticket import GetUserResponed,GetUserTicketMessageRespones
import uuid
from api.responses.BaseMessage import BaseMessage
from datetime import datetime
import pytz
router = APIRouter(prefix="/api/v1/ticket")
from cryptography.fernet import Fernet
#Token
#access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET=b'BH4aRBCP4jjunyjAYA64zQst1ROAW34BlbtWpvhJdKo=' 

fernet=Fernet(SECRET)
#from cryptography.fernet import Fernet


@router.post("/",response_model=BaseMessage)
def create_ticket(req:CreateTicketRequest,db:Session=Depends(get_db)):#credintial
    if req is None:
        raise HTTPException(status_code=400,detail="داده ورودی معتبر نمی باشد")
    if len(req.text) <1:
        raise HTTPException(status_code=400,detail="متن را وارد کنید")
    if len(req.subject) <1:
        raise HTTPException(status_code=400,detail="عنوان را وارد کنید")
    #grftan id user
    #userID=uuid.UUID(credentials["id"]).hex
    #                                   user id
    encryptCreator = fernet.encrypt(req.creator)
    encyptedSubject=fernet.encrypt( req.subject)
    encyptedText = fernet.encrypt(req.text)
    New_Ticket=ticket.create_ticket(db,encryptCreator,encyptedSubject,encyptedText)
    #                                                       user id
    ticket_messeage=ticket.create_ticket_meesage(db,New_Ticket.id,encyptedText)

    # payam baraye admin

    # for contrib in req.contributers:
    #     user= account.get_user(db,contrib)
    #     if user is None:
    #         continue
    #     track.create_contributer(db,newtrack.id,contrib,False)
    return BaseMessage(message="پیگیری با موفقیت ثبت شد")

@router.get("/all")
def GetAllTickts(db:Session=Depends(get_db)):#credintial
    #admin ? 
    #id user
    data= ticket.get_tickets(db)

    response=[]
    for item in data:

        response.append( GetUserResponed(
            
            id=item.id,
            decryptedSubject=fernet.decrypt(item.subject),
            decryptedStartDate=fernet.decrypt(item.startDate),
            decryptedCreatedAt=fernet.decrypt(item.createAt),
            decryptedLocked=fernet.decrypt(item.locked),
            decryptedCreator=fernet.decrypt(item.creator)
        ))
    return response


@router.patch("/",status_code=200,response_model=BaseMessage)
def EditTicketRequest(req :EditTicketRequest,db: Session = Depends(get_db)):#credintial
    
    if len(req.subject) < 1:
        raise HTTPException(status_code=400,detail=" عنوان را وارد کنید")
    if len(req.text) < 1:
        raise HTTPException(status_code=400,detail="  متن مورد نظر را وارد کنید")

    #creator =  uuid.UUID( credentials['id']).hex 
    getTicket=ticket.get_tickets(db,req.id)
    if getTicket is None:
        raise HTTPException(status_code=404,detail="پیگیری مورد نظر یافت نشد")
    # if getTicket.creator!=creator:
    #     raise HTTPException(status_code=404,detail="پیگیری مورد نظر یافت نشد")

    getTicket.subject=req.subject
    getTicket.text=req.text
    # time ?
    db.commit()
    
    # chek krdn khali nbodn reciver


    # for contrib in req.contributers:
    #     user= account.get_user(db,contrib)
    #     if user is None:
    #         continue
    #     track.create_contributer(db,getTrack.id,contrib,False)
    return BaseMessage(message="تغییرات پیگیری با موفقیت ثبت شد")


@router.post("/message",status_code=200,response_model=BaseMessage)
def CreateTicketMessege(req:CreateTicketMessegeRequest,db:Session=Depends(get_db)):#credintial
   # user ID
   getTicket=ticket.get_tickets(db,req.ticket)
   if getTicket is None:
        raise HTTPException(status_code=404,detail="پیگیری مورد نظر یافت نشد")
#create reciver
#check reciver
#userid
   encryptTicketID = fernet.encrypt(req.ticketID)
   encryptCreator = fernet.encrypt(req.creator)
   encryptText = fernet.encrypt(req.Text)
   ticket.create_ticket_meesage(db,encryptCreator,encryptText,encryptTicketID)

   return BaseMessage(message="پیام شما با موفقیت ثبت شد")
    

#route get ticket_message
@router.get("/{id}",response_model=TrackResponse)
def getTicketMessage(id:int,db:Session=Depends(get_db)):#credential
#userid
    response=[]
    TicketMessage = ticket.get_ticket_message(db,TicketMessage.id)
    for item in TicketMessage:
        response.append( GetUserTicketMessageRespones(
        
            decryptedTicketID = fernet.decrypt(item.TicketID),
            decryptedAccountID = fernet.decrypt(item.accountID),
            decryptedCreatedAt = fernet.decrypt(item.createAt),
            decryptedText = fernet.decrypt(item.text)
        ))
    return response
@router.patch("/message",status_code=200,response_model=BaseMessage)
def EditTicketkMessage(req :EditTrackMessage,db: Session = Depends(get_db)):#credential
    TicketMessage = ticket.get_ticket_message(db,TicketMessage.id)
    #userID 
    #check messege
    #check id
    #check len
    encryptedText = fernet.encrypt(req.text)
    db.commit()
    return BaseMessage(message="تغییرات پیگیری با موفقیت ثبت شد")


