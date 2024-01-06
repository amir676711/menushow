from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.category import createCategoryRequest

def Create_Category(db: Session,user=createCategoryRequest):
    db_new_category = models.Category(faName=user.faName,enName=user.enName,storeID=user.StoreID)
    db.add(db_new_category)
    db.commit()
    db.refresh(db_new_category)
    return db_new_category

def get_AllDetailcategory(db:Session):
    return db.query(models.Category).all()

def get_category_by_StoreID(db:Session,storeID:int):
    return db.query(models.Category).filter(models.Category.storeID == storeID).first()
def get_category_by_ID(db:Session,storeID:int):
    return db.query(models.Category).filter(models.Category.id == id).first()

