from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.city import CreateCityRequest

def CreateCity(db: Session,user=CreateCityRequest):
    db_city = models.city(faName=user.faName,enName=user.enName)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db:Session,id:int):
    return db.query(models.city).filter(models.city.id == id).first()

