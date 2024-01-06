from sqlalchemy import Boolean, Column, ForeignKey,Double, Integer, String,UUID,DateTime,Double
from sqlalchemy.orm import relationship
import uuid
from .database import Base
from .Types import BinaryUUID
from datetime import datetime

class Account(Base):
    __tablename__ = "accounts"
    id = Column('id',BinaryUUID, primary_key=True, index=True,default=uuid.uuid4)
    fName = Column(String(300))
    lName = Column(String(300))
    password = Column(String(300))
    tell=Column(String(15),unique=True)
    activePlanId=Column(Integer)
    createAt=Column(DateTime)
    planActiveDate=Column(DateTime)
    expireDate=Column(DateTime)
    reffralCode=Column(String(10))
    reagentCode=Column(String(10))
    lastLogin=Column(DateTime)
    isAdmin = Column(Boolean, default=False)
    
#reffralCode
#expireDate
#activePlanId
class Store (Base):
    __tablename__ = "store"
    id = Column(Integer, primary_key=True, index=True)
    faName=Column(String(200))
    enName=Column(String(200))
    address = Column(String(200))
    lat = Column(Double)
    lon = Column(Double)
    logoUrl=Column(String(500))
    priceUnit=Column(String(300))
    cityID = Column(Integer)
    storeType = Column(Integer)
    hasDelivery = Column(Boolean,default=False)
    hasWiFi = Column(Boolean, default=False)
    tell = Column(String(13))
    whatsappID = Column(String(20))
    instagramID = Column(String(20))
    telegramID=Column(String(300))

class province(Base):
    __tablename__='provine'
    id = Column(Integer, primary_key=True, index=True)
    faName = Column(String(200))
    enName = Column(String(200))

class city(Base):
    __tablename__='City'
    id = Column(Integer, primary_key=True, index=True)
    provinceID = Column(Integer)
    faName = Column(String(200))
    enName = Column(String(200))

class Category(Base):
    __tablename__='Category'
    faName = Column(String(200))
    enName = Column(String(200))
    storeID = Column(Integer, primary_key=True, index=True)
    # icon = Column(String(5000))
    

class Ticket(Base):
    __tablename__='ticket'
    id = Column(Integer,primary_key=True,index=True)
    subject = Column(String(300))
    startDate = Column(DateTime)
    createAt = Column(DateTime)
    locked=Column(Boolean,default=False)
    creator = Column('creator',BinaryUUID,default=uuid.uuid4)


class TicketMessage(Base):
    __tablename__='TicketMessage'
    id = Column(Integer,primary_key=True,index=True)
    TicketID=Column(Integer)
    accountID = Column('accountID',BinaryUUID,default=uuid.uuid4)
    text=Column(String(3000))
    createdAt= Column(DateTime)
    #fileupload=Column(String(3000))

class Food(Base):
    __tablename__='food'
    id = Column(Integer,primary_key=True,index=True)
    faName = Column(String(20))
    enName = Column(String(20))
    AmountOfFood = Column(String(10))
    DiscountPercent = Column(Integer)
    Status = Column(Boolean,default=False)
    CategoryID = Column(Integer)
    faDescription = Column(String(3000))
    enDescription = Column(String(3000))
    Description = Column(String(3000))
    itemMode = Column(String(20))
    Title = Column(String(20))
    Price = Column(String(10))
    #foodIcon
    #foodPicture

class Slider(Base):
    __tablename__='Slider'
    id=Column(Integer,primary_key=True,index=True)
    Picture = Column(String(3000))
    Number = Column(Integer)


class Menu(Base):
    __tablename__='Menu'
    id = Column(Integer,primary_key=True,index=True)
    ResturantName = Column(String(20))
    LogoUrl = Column(String(5000))
    BackgroundPicture = Column(String(5000))
    graphicUrl = Column(String(5000))
    PhoneNumber = Column(Integer)
    Address = Column(String(50))

# class Agenda(Base):
#     __tablename__='Agenda'
#     StartDate = Column(datetime)
#     EndDate = Column(datetime)

class Theme(Base):
    __tablename__='Theme'
    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(20))
    ThemeUrl = Column(String(3000))
    Price = Column(String(10))


class Pager(Base):
    __tablename__='Pager'
    id = Column(Integer,primary_key=True,index=True)
    ShowPager = Column(String(30))
    NumberSMS = Column(String(15))
    RequestPager = Column(String(3000))

# class Rate(Base):
#     __tablename__='Rate'
#     id= Column(Integer,primary_key=True,index=True)
#     ShowRate = Column(Integer)
#     RateText =  Column(String(3000))

# class Plan(Base):
#     __tablename__='Plan'
#     id = Column(Integer)
#     title = Column(String(50))
#     days = Column(Integer)
#     price = Column(String(20))

# class comment(Base):
#     __tablename__='Comment'
#     id = Column(Integer)
#     title = Column(String(50))
#     text = Column(String(3000))
#     accountID = Column('accountID',BinaryUUID,default=uuid.uuid4)