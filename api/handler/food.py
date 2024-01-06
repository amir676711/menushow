from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.food import CreateFoodRequest,EditFoodRequest
from api.response.food import foodRespones
from database.CRUD import food


router = APIRouter(prefix="/api/v1/food")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewFood(req : CreateFoodRequest,db: Session = Depends(get_db)):
    new_food = food.create_food(db,req)
    if new_food is None :
        raise HTTPException(status_code=400,detail="در ثبت غذا خطا رخ داده است")
    return BaseMessage(message="غذا جدید با موفقیت ثبت شد")

@router.get("/")
def GetAllFood(db:Session=Depends(get_db)):
    get_Allfood= food.get_food(db)
    if get_Allfood is None:
        raise HTTPException(status_code=404,detail="غذاهای مورد نظر یافت نشد")
    return get_Allfood


@router.get("/{id}")
def GetFoodDetail(id:int,db:Session=Depends(get_db)):
    gfood= food.get_food_by_ID(db,id)
    if gfood is None:
        raise HTTPException(status_code=404,detail="غذا مورد نظر یافت نشد")
    return foodRespones(faName=gfood.faName,enName=gfood.enName,AmountOfFood=gfood.AmountOfFood,DiscountPercent=gfood.DiscountPercent,Status=gfood.Status,CategoryID=gfood.CategoryID,faDescription=gfood.faDescription,enDescription=gfood.enDescription,Description=gfood.Description,itemMode=gfood.itemMode,Title=gfood.Title,Price=gfood.Price)

@router.patch("/",status_code=201,response_model=BaseMessage)
def EditFood(req:EditFoodRequest,db : Session = Depends(get_db)):
    food_Edit = food.get_food(db)
    if food_Edit is None:
        HTTPException(status_code=400,detail="در تغییر اطلاعات کاربر خطا رخ داده است")
    food_Edit.faName=req.faName
    food_Edit.enName=req.enName
    food_Edit.AmountOfFood=req.AmountOfFood
    food_Edit.DiscountPercent=req.DiscountPercent
    food_Edit.Status=req.Status
    food_Edit.CategoryID=req.CategoryID
    food_Edit.faDescription=req.faDescription
    food_Edit.enDescription=req.enDescription
    food_Edit.Description=req.Description
    food_Edit.itemMode=req.itemMode
    food_Edit.Title=req.Title
    food_Edit.price=req.Price
    db.commit()
    return BaseMessage(message="تغییرات با موفقیت انجام شد")

@router.delete("/{id}",response_model=BaseMessage)
def DeleteFood(id:int,db:Session=Depends(get_db)):
    food=food.get_food_by_ID(db,id)
    if food is None :
        raise HTTPException(status_code=404,detail="غذای مورد نظر یافت نشد")
    if not food.delete_food_byID(db,id) :
        raise HTTPException(status_code=400,detail="در حذف غذا خطا رخ داده است")
    return BaseMessage(message="غذای مورد نظر با موفقیت حذف شد")