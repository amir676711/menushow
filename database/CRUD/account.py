from sqlalchemy import and_,or_
from uuid import UUID,uuid4
from sqlalchemy.orm import Session
import hashlib
from database import models
from api.request.account import CreateUserRequest,EditUserRequst,LoginUserRequest
from cryptography.fernet import Fernet 
from datetime import datetime,timedelta
import random

def get_by_tell(db:Session,tell:str):
    return db.query(models.Account).filter(models.Account.tell==tell).first()
def get_by_id(db:Session,id:UUID):
    return db.query(models.Account).filter(models.Account.id==id).first()
def get_all(db:Session):
    return db.query(models.Account).all()

def login_user(db: Session, tell:int,password:str ):
    hashed_password = hashlib.md5(password.encode('utf-8'))
    print(hashed_password)
    return db.query(models.Account).filter(and_(models.Account.tell == tell , models.Account.password== hashed_password.hexdigest())).first()


def create_user(db: Session, fName:str ):
    hashed_password = hashlib.md5(user.password.encode('utf-8'))
    generatedID=uuid4()
    code=0
    while code==0:
        chars =  string.digits
        random.seed = (os.urandom(1024))

        code= ''.join(random.choice(chars) for i in range(5))
        user=db.query(models.Account).filter(models.Account.reffralCode==code).first()
        if user !=None:
            code=0

    db_user = models.Account(id=generatedID,fName=fName,lName=user.lName,isAdmin=user.isAdmin,reagentCode=user.reagentCode,password=hashed_password.hexdigest(),tell=user.tell,planActiveDate=datetime.now(),activePlanId=0,expireDate=datetime.now()+timedelta(days=7))
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session,user_id:UUID):
    try:
        user=db.query(models.Account).filter(models.Account.id == user_id).first()
        db.delete(user)
        db.commit()
    except:
        return False
    return True
        