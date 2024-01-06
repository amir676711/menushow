from sqlalchemy import or_
from sqlalchemy.orm import Session
from database import models
from datetime import datetime
from uuid import UUID
from api.request.food import CreateFoodRequest


def create_food(db:Session,user_food:CreateFoodRequest):
    db_food = models.Food(faName=user_food.faName,enName=user_food.enName,AmountOfFood=user_food.AmountOfFood,DiscountPercent=user_food.DiscountPercent,Status=user_food.Status,CategoryID=user_food.CategoryID,faDescription=user_food.faDescription,enDescription=user_food.enDescription,Description=user_food.Description,itemMode=user_food.itemMode,Title=user_food.Title,Price=user_food.Price)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def get_food(db:Session):
    return db.query(models.Food).all()

def get_food_by_ID(db:Session,id:int):
    return db.query(models.Food).filter(models.Food.id==id).first()

def delete_food_byID(db:Session,id:int):
    try:
        user_food=db.query(models.Food).filter(models.Food.id == id).first()
        db.delete(user_food)
        db.commit()
    except:
        return False
    return True
        