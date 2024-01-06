from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.theme import createThemeRequest,EditThemeRequest
from api.response.theme import CreateThemeRespones
from database.CRUD import theme

router = APIRouter(prefix="/api/v1/theme")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewTheme(req : createThemeRequest,db: Session = Depends(get_db)):
    new_Theme = theme.create_theme(db,req)
    if new_Theme is None :
        raise HTTPException(status_code=400,detail="در ثبت تم جدید خطا رخ داده است")
    return BaseMessage(message="تم جدید با موفقیت ثبت شد")

@router.get("/{id}")
def GetThemeDetail(id:int,db:Session=Depends(get_db)):
    get_themeID= theme.get_Theme_byID(db,id)
    if get_themeID is None:
        raise HTTPException(status_code=404,detail="تم مورد نظر یافت نشد")
    return CreateThemeRespones(id=get_themeID.id,Name=get_themeID.Name,ThemeUrl=get_themeID.ThemeUrl,Price=get_themeID.Price)


@router.get("/")
def GetThemeAll(db:Session=Depends(get_db)):
    get_ALlTheme= theme.get_Theme(db)
    if get_ALlTheme is None:
        raise HTTPException(status_code=404,detail="تم مورد نظر یافت نشد")
    return get_ALlTheme


@router.patch("/",status_code=201,response_model=BaseMessage)
def EditTheme(req:EditThemeRequest,db : Session = Depends(get_db)):
    themeall = theme.get_Theme_byID(db,req.id)
    if theme_name is None:
        HTTPException(status_code=400,detail="در تغییر نم کاربر خطا رخ داده است")
    themeall.Name=req.Name
    themeall.ThemeUrl=req.ThemeUrl
    themeall.id=req.id
    db.commit()
    return BaseMessage(message="تغییرات با موفقیت انجام شد")