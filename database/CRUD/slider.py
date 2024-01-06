from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.slider import CreateSliderRequest,EditSliderRequest


def create_Slider(db:Session,slider:CreateSliderRequest):
    db_slider = models.Slider(Picture=slider.Picture,Number=slider.Number)
    db.add(db_slider)
    db.commit()
    db.refresh(db_slider)
    return db_slider

def get_Slider(db:Session):
    return db.query(models.Slider).all()

def get_Slider_by_ID(db:Session,id:int):
    return db.query(models.Slider).filter(models.Slider.id==id).first()

def delete_Slider_byID(db:Session,id:int):
    try:
        user_slider=db.query(models.Slider).filter(models.Slider.id == id).first()
        db.delete(user_slider)
        db.commit()
    except:
        return False
    return True
        