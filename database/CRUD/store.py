from sqlalchemy import and_,or_
from uuid import UUID,uuid4
from sqlalchemy.orm import Session
import hashlib
from database import models
from api.request.store import CreateStoreRequest,EditStoreUser



def createStore(db: Session,user=CreateStoreRequest):
    db_store = models.Store(faName=user.faName,enName=user.enName,address=user.address,lat=user.lat,lon=user.lon,logoUrl=user.logoUrl,priceUnit=user.priceUnit,cityID=user.cityID,storeType=user.storeType,hasDelivery=user.hasDelivery,hasWiFi=user.hasWiFi,whatsappID=user.whatsappID,telegramID=user.telegramID,instagramID=user.instagramID,tell=user.tell)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def get_Store(db:Session):
    return db.query(models.Store).all()

def get_store_by_id(db:Session,id:int):
    return db.query(models.Store).filter(models.Store.id == id).first()

def delete_store_user(db:Session,store_id:UUID):
    try:
        user_store=db.query(models.Store).filter(models.Store.id == id).first()
        db.delete(user_store)
        db.commit()
    except:
        return False
    return True
        