from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.category import createCategoryRequest,EditcategoryRequest
from api.response.category import categoryRespones
from database.CRUD import category

router = APIRouter(prefix="/api/v1/category")

#access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewcategory(req : createCategoryRequest,db: Session = Depends(get_db)):
    new_category = category.Create_Category(db,req)
    if new_category is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات کاربر جدید خطا رخ داده است")
    return BaseMessage(message="دسته بندی جدید با موفقیت ثبت شد")


@router.get("/")
def GetCategory(db:Session=Depends(get_db)):
    get_category= category.get_AllDetailcategory(db)
    if get_category is None:
        raise HTTPException(status_code=404,detail="دسته بندی مورد نظر یافت نشد")
    return get_category

@router.get("/{storeID}",status_code=201)
def GetAllcategory(storeID:int,db:Session=Depends(get_db)):
    cats = category.get_category_by_StoreID(db,storeID)
    response=[]
    for item in cats:

        response.append( categoryRespones(
            
            id=item.id,
            faName=item.faName,
            enName=item.enName,
            storeID=item.storeID
        ))
    return response



@router.patch("/",status_code=201,response_model=BaseMessage)
def EditCategory(req:EditcategoryRequest,db : Session = Depends(get_db)):
    categoryEdit = category.get_category_by_StoreID(db,req.StoreID)
    if categoryEdit is None:
        HTTPException(status_code=400,detail="در تغییر اطلاعات کاربر خطا رخ داده است")
    categoryEdit.faName=req.faName
    categoryEdit.enName=req.enName
    categoryEdit.StoreID=req.StoreID
    db.commit()
    return BaseMessage(message="تغییرات با موفقیت انجام شد")