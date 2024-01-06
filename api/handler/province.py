from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.province import CreateprovinceRequest,EditprovinceRequest
from api.response.province import provinceResponse
from database.CRUD import province

router = APIRouter(prefix="/api/v1/province")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewProvince(req : CreateprovinceRequest,db: Session = Depends(get_db)):
    new_province_USEr = province.create_province(db,req)
    if new_province_USEr is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات کاربر جدید خطا رخ داده است")
    return BaseMessage(message="استان جدید با موفقیت ثبت شد")


@router.get("/{id}")
def GetProvinceDetail(id:int,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security) ):
    get_province= province.get_province(db,id)
    if get_province is None:
        raise HTTPException(status_code=404,detail="نقش مورد نظر یافت نشد")
    return get_province


@router.patch("/",status_code=201,response_model=BaseMessage)
def Editprovince(req:EditprovinceRequest,db : Session = Depends(get_db)):
    province_name = province.get_province(db,req)
    if province_name is None:
        HTTPException(status_code=400,detail="در تغییر اطلاعات کاربر خطا رخ داده است")
    return BaseMessage(message="تغییرات با موفقیت انجام شد")