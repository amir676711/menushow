from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.pager import CreatePagerRequest

def Createpager(db: Session,user=CreatePagerRequest):
    db_pager = models.Pager(ShowPager=user.ShowPager,NumberSMS=user.NumberSMS,RequestPager=user.RequestPager)
    db.add(db_pager)
    db.commit()
    db.refresh(db_pager)
    return db_pager

def get_pager(db:Session):
    return db.query(models.Pager).all()

def get_pager_byID(db:Session,id:int):
    return db.query(models.Pager).filter(models.Pager.id == id).first()

