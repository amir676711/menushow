from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.menu import CreateMenuRequest,EditMenuRequest
from api.response.menu import menuRespones
from database.CRUD import menu


router = APIRouter(prefix="/api/v1/menu")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewMenu(req : CreateMenuRequest,db: Session = Depends(get_db)):
    new_menu = menu.create_menu(db,req)
    if new_menu is None :
        raise HTTPException(status_code=400,detail="در ثبت منو خطا رخ داده است")
    return BaseMessage(message="منو جدید با موفقیت ثبت شد")

@router.get("/")
def GetAllMenu(db:Session=Depends(get_db)):
    get_AllMenu= menu.get_menu(db)
    if get_AllMenu is None:
        raise HTTPException(status_code=404,detail="منوهای مورد نظر یافت نشد")
    return get_AllMenu


@router.get("/{id}")
def GetMenuDetail(id:int,db:Session=Depends(get_db)):
    gt_menu= menu.get_menu_by_ID(db,id)
    if gt_menu is None:
        raise HTTPException(status_code=404,detail="منو مورد نظر یافت نشد")
    return menuRespones(ResturantName=gt_menu.ResturantName,LogoUrl=gt_menu.LogoUrl,Address=gt_menu.Address,PhoneNumber=gt_menu.PhoneNumber,BackgroundPicture=gt_menu.BackgroundPicture,graphicUrl=gt_menu.graphicUrl)

@router.patch("/",status_code=201,response_model=BaseMessage)
def EditMenu(req:EditMenuRequest,db : Session = Depends(get_db)):
    Menu_Edit = menu.get_menu_by_ID(db,req.id)
    if Menu_Edit is None:
        HTTPException(status_code=400,detail="در تغییر اطلاعات منو خطا رخ داده است")
    Menu_Edit.ResturantName=req.ResturantName
    Menu_Edit.LogoUrl=req.LogoUrl
    Menu_Edit.Address=req.Address
    Menu_Edit.PhoneNumber=req.PhoneNumber
    Menu_Edit.BackgroundPicture=req.BackgroundPicture
    Menu_Edit.graphicUrl=req.graphicUrl
    db.commit()
    return BaseMessage(message="تغییرات با موفقیت انجام شد")

@router.delete("/{id}",response_model=BaseMessage)
def DeleteMenu(id:int,db:Session=Depends(get_db)):
    menu_D=menu.get_menu_by_ID(db,id)
    if menu_D is None :
        raise HTTPException(status_code=404,detail="منو مورد نظر یافت نشد")
    if not menu.delete_menu_byID(db,id) :
        raise HTTPException(status_code=400,detail="در حذف منو خطا رخ داده است")
    return BaseMessage(message="منوی مورد نظر با موفقیت حذف شد")