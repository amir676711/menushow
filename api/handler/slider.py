from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.slider import CreateSliderRequest,EditSliderRequest
from api.response.slider import CreateSliderRespones
from database.CRUD import slider


router = APIRouter(prefix="/api/v1/slider")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewSlider(req : CreateSliderRequest,db: Session = Depends(get_db)):
    new_slider = slider.create_Slider(db,req)
    if new_slider is None :
        raise HTTPException(status_code=400,detail="در ثبت اسلاید خطا رخ داده است")
    return BaseMessage(message="اسلاید جدید با موفقیت ثبت شد")

@router.get("/")
def GetAllSlider(db:Session=Depends(get_db)):
    get_AllSlider= slider.get_Slider(db)
    if get_AllSlider is None:
        raise HTTPException(status_code=404,detail="اسلایدهای مورد نظر یافت نشد")
    return get_AllSlider


@router.get("/{id}")
def GetSliderDetail(id:int,db:Session=Depends(get_db)):
    get_AllSlider= slider.get_Slider_by_ID(db,id)
    if get_AllSlider is None:
        raise HTTPException(status_code=404,detail="اسلاید مورد نظر یافت نشد")
    return CreateSliderRespones(id=get_AllSlider.id,Picture=get_AllSlider.Picture,Number=get_AllSlider.Number)

# @router.patch("/",status_code=201,response_model=BaseMessage)
# def EditSlider(req:EditSliderRequest,db : Session = Depends(get_db)):
#     Slider_Edit = slideri.get_Slider(db)
#     if Slider_Edit is None:
#         HTTPException(status_code=400,detail="در تغییر اطلاعات کاربر خطا رخ داده است")
#     Slider_Edit.Picture = req.Picture
#     Slider_Edit.Number = req.Number
#     db.commit()
#     return BaseMessage(message="تغییرات با موفقیت انجام شد")

@router.delete("/{id}",response_model=BaseMessage)
def DeleteSlide(id:int,db:Session=Depends(get_db)):
    slide=slider.get_Slider_by_ID(db,id)
    if slide is None :
        raise HTTPException(status_code=404,detail="اسلاید مورد نظر یافت نشد")
    if not slider.delete_Slider_byID(db,id) :
        raise HTTPException(status_code=400,detail="در حذف اسلاید خطا رخ داده است")
    return BaseMessage(message="اسلاید مورد نظر با موفقیت حذف شد")