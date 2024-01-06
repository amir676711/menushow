from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.menu import CreateMenuRequest


def create_menu(db:Session,user_menu:CreateMenuRequest):
    db_menu = models.Menu(ResturantName=user_menu.ResturantName,LogoUrl=user_menu.LogoUrl,BackgroundPicture=user_menu.BackgroundPicture,graphicUrl=user_menu.graphicUrl,PhoneNumber=user_menu.PhoneNumber,Address=user_menu.Address)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def get_menu(db:Session):
    return db.query(models.Menu).all()

def get_menu_by_ID(db:Session,id:int):
    return db.query(models.Menu).filter(models.Menu.id==id).first()

def delete_menu_byID(db:Session,id:int):
    try:
        user_menu=db.query(models.Menu).filter(models.Menu.id == id).first()
        db.delete(user_menu)
        db.commit()
    except:
        return False
    return True
        