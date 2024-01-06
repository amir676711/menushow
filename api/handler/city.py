from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.city import CreateCityRequest,EditcityRequest
from api.response.city import cityRespones
from database.CRUD import province,city

router = APIRouter(prefix="/api/v1/city")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewcity(req : CreateCityRequest,db: Session = Depends(get_db)):
    new_city_USEr = city.CreateCity(db,req)
    if new_city_USEr is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات کاربر جدید خطا رخ داده است")
    return BaseMessage(message="شهر جدید با موفقیت ثبت شد")


@router.get("/{id}")
def GetcityDetail(id:int,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security) ):
    get_city= city.get_city(db,id)
    if get_city is None:
        raise HTTPException(status_code=404,detail="شهر مورد نظر یافت نشد")
    return get_city


@router.patch("/",status_code=201,response_model=BaseMessage)
def Editcity(req:EditcityRequest,db : Session = Depends(get_db)):
    city_name = city.get_city(db,req.id)
    if city_name is None:
        HTTPException(status_code=400,detail="در تغییر اطلاعات کاربر خطا رخ داده است")
    city_name.provinceID=req.id
    db.commit()
    return BaseMessage(message="تغییرات با موفقیت انجام شد")