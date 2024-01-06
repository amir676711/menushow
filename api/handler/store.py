from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import services.jwt as jwt
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from api.request.store import CreateStoreRequest,EditStoreUser
from api.response.store import storeRespones
from database.CRUD import store

router = APIRouter(prefix="/api/v1/store")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",status_code=201,response_model=BaseMessage)
def createNewStore(req : CreateStoreRequest,db: Session = Depends(get_db)):
    new_Store = store.createStore(db,req)
    if new_Store is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات فروشگاه جدید خطا رخ داده است")
    return BaseMessage(message="فروشگاه جدید با موفقیت ثبت شد")

@router.get("/")
def GetStoreAll(db:Session=Depends(get_db)):
    get_store= store.get_Store(db)
    if get_store is None:
        raise HTTPException(status_code=404,detail="فروشگاه مورد نظر یافت نشد")
    return get_store

# @router.get("/all")
# def getStore(db:Session=Depends(get_db)):#credential
# #userid
#     response=[]
#     getstore = store.get_Store(db)
#     for item in getstore:
#         response.append( storeRespones(
        
#             id = item.id,
#             faName=item.faName,
#             enName=item.enName,
#             address=item.address,
#             tell=item.tell,
#             lat=item.lat,
#             lon=item.lon,
#             logoUrl=item.logoUrl,
#             priceUnit=item.priceUnit,
#             cityID=item.cityID,
#             storeType=item.storeType,
#             hasDelivery=item.hasDelivery,
#             hasWiFi=item.hasWiFi,
#             whatsappID=item.whatsappID,
#             instagramID = item.instagramID,
#             telegramID = item.telegramID
#         ))
#     return response





@router.get("/{id}",status_code=200)
def GetUserStore(id:int,db:Session=Depends(get_db)):#credential
#userid
    item = store.get_store_by_id(db,id)
    print(item)
    if item is None:
        raise HTTPException(status_code=404,detail="فروشگاه یافت نشد")
    return storeRespones(
    
        id = item.id,
        faName=item.faName,
        enName=item.enName,
        address=item.address,
        tell=item.tell,
        lat=item.lat,
        lon=item.lon,
        logoUrl=item.logoUrl,
        priceUnit=item.priceUnit,
        cityID=item.cityID,
        storeType=item.storeType,
        hasDelivery=item.hasDelivery,
        hasWiFi=item.hasWiFi,
        whatsappID=item.whatsappID,
        instagramID=item.instagramID,
        telegramID=item.telegramID
    )
    

@router.delete("/{id}",response_model=BaseMessage)
def DeleteStore(id:UUID,db:Session=Depends(get_db)):
    user_store=store.get_store_by_id(db,id)
    if user is None :
        raise HTTPException(status_code=404,detail="فروشگاه مورد نظر یافت نشد")
    if not store.delete_store_user(db,id) :
        raise HTTPException(status_code=400,detail="در حذف فروشگاه خطا رخ داده است")
    return BaseMessage(message="فروشگاه مورد نظر با موفقیت حذف شد")

@router.patch("/",status_code=200,response_model=BaseMessage)
def EditStoreUSer(req:EditStoreUser, db:Session=Depends(get_db)):
    #admin
    user=store.get_store_by_id(db,req.id)
    if user is None :
        raise HTTPException(status_code=404,detail="فروشگاه مورد نظر یافت نشد")
    # user.id=req.id
    user.faName=req.faName
    user.enName=req.enName
    user.address=req.address
    user.tell=req.tell
    user.lat=req.lat
    user.lon=req.lon
    user.logoUrl=req.logoUrl
    user.priceUnit=req.priceUnit
    user.cityID=req.cityID
    user.storeType=req.storeType
    user.hasDelivery=req.hasDelivery
    user.hasWiFi=req.hasWiFi
    user.telegramID=req.telegramID
    user.instagramID=req.instagramID
    user.whatsappID=req.whatsappID
    db.commit()
    return BaseMessage(message="اطلاعات فروشگاه با موفقیت ویرایش شد")