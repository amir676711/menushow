from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.pager import CreatePagerRequest,EditPagerRequest
from api.response.pager import pagerRespones
from database.CRUD import pager

router = APIRouter(prefix="/api/v1/pager")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewpager(req : CreatePagerRequest,db: Session = Depends(get_db)):
    new_pager = pager.Createpager(db,req)
    if new_pager is None :
        raise HTTPException(status_code=400,detail="در ثبت پیجر جدید خطا رخ داده است")
    return BaseMessage(message="پیجر جدید با موفقیت ثبت شد")


@router.get("/")
def GetpagerDetail(db:Session=Depends(get_db)):
    get_pager= pager.get_pager(db)
    if get_pager is None:
        raise HTTPException(status_code=404,detail="پیجر مورد نظر یافت نشد")
    return get_pager

@router.get("/{id}")
def GetpagerDetail(id:int,db:Session=Depends(get_db)):
    get_pagerDetail= pager.get_pager_byID(db,id)
    if get_pagerDetail is None:
        raise HTTPException(status_code=404,detail="پیجر مورد نظر یافت نشد")
    return pagerRespones(id=get_pagerDetail.id,ShowPager=get_pagerDetail.ShowPager,NumberSMS=get_pagerDetail.NumberSMS,RequestPager=get_pagerDetail.RequestPager)

