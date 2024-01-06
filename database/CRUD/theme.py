from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.theme import createThemeRequest

def create_theme(db: Session, user: createThemeRequest):
    db_Theme = models.Theme(name=user.Name,ThemeUrl=user.ThemeUrl,Price=user.Price)
    db.add(db_Theme)
    db.commit()
    db.refresh(db_Theme)
    return db_Theme

def get_Theme(db:Session):
    return db.query(models.Theme).all()

def get_Theme_byID(db:Session,id:int):
    return db.query(models.Theme).filter(models.Theme.id == id).first()

