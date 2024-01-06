from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.province import CreateprovinceRequest

def create_province(db: Session, user: CreateprovinceRequest):
    db_province = models.province(faName=user.faName,enName=user.enName)
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province


def get_province(db:Session,id:int):
    return db.query(models.province).filter(models.province.id == id).first()

