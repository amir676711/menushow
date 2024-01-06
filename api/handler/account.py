from fastapi import APIRouter,Body,Depends,HTTPException, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from sqlalchemy.orm import Session
from database.database import SessionLocal
from uuid import UUID
import hashlib
import services.jwt as jwt
from datetime import datetime
from api.request.account import CreateUserRequest,LoginUserRequest,EditUserRequst,EditUSerByAdmin,UserPasswordChangeRequest
from api.response.account import UserLoginResponse,GetUsersDetailResponed
from database.CRUD import account
from api.response.BaseMessage import BaseMessage
from datetime import timedelta
from cryptography.fernet import Fernet

SECRET=b'BH4aRBCP4jjunyjAYA64zQst1ROAW34BlbtWpvhJdKo=' 

fernet=Fernet(SECRET)

router = APIRouter(prefix="/api/v1/account")

access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewUser(req : CreateUserRequest,db: Session = Depends(get_db)):
    # accountcheck=account.get_by_tell(db,req.tell)
    # if accountcheck is not None:
    #     raise HTTPException(status_code=404,detail=" شما قبلا ثبت نام کرده اید")
    

    encyptedFName=fernet.encrypt(bytes( req.fName,'utf-8'))

    newUser= account.create_user(db,encyptedFName)
    if newUser is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات کاربر جدید خطا رخ داده است")
    return BaseMessage(message="کاربر جدید با موفقیت ثبت شد")


########reagentCode

@router.get("/{id}")
def GetUserDetail(id:UUID,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security) ):
    if credentials['isAdmin'] == "False":
        raise HTTPException(status_code=403,detail="دسترسی شما محدود شده است")

    item = account.get_user(db,id)
    #check kardan inke user dar database bashad
    if item is None:
        raise HTTPException(status_code=404,detail="کاربر مورد نظر یافت نشد")
    grole=role.get_role(db,item.roleID)

    return AccountDetailResponse(ID=item.id ,FName=item.fName ,LName=item.lName ,EmpCode=item.empCode ,RoleID=item.roleID ,isAdmin=item.isAdmin ,Tell=item.tell ,codeMelli=item.codeMelli,RoleName=grole.title)

# @router.get("/{id}")
# def GetUserDetail(id:UUID,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security) ):
#     # if credentials['isAdmin'] == "False":
#     #     raise HTTPException(status_code=403,detail="دسترسی شما محدود شده است")
    
#     item = account.get_by_id(db,id)
#     if item is None:
#         raise HTTPException(status_code=404,detail="کاربر مورد نظر یافت نشد")
#     # grole=role.get_role(db,item.roleID)
    
#     return GetUsersDetailResponed(FullName=f"{item.fName} {item.lName}",id=item.id,isAdmin=item.isAdmin,tell=item.tell,reagentCode=item.reagentCode)


@router.post("/login",status_code=201,response_model=UserLoginResponse)
def login_user(req: LoginUserRequest,db:Session= Depends(get_db)):
    # if credentials['isAdmin'] == "False":
    #     raise HTTPException(status_code=404,detail="دسترسی شما محدود است")
    user = account.login_user(db,req.tell,req.password)
    if user is None :
        raise HTTPException(status_code=404,detail="کاربر با مشخصات وارد شده یافت نشد")
    user.lastLogin=datetime.now()
    db.commit()
    subject={'id':str(user.id),'fname':user.fName,'lname':user.lName}
    token=access_security.create_access_token(subject=subject,expires_delta=timedelta(hours=1))
    return UserLoginResponse(FullName=f"{user.fName} {user.lName}",isAdmin=user.isAdmin,tell=user.tell,reagentCode=user.reagentCode,token=token)

@router.delete("/{id}",response_model=BaseMessage)
def DeleteUser(id:UUID,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security)):
    user=account.get_by_id(db,id)
    if user is None :
        raise HTTPException(status_code=404,detail="کاربر مورد نظر یافت نشد")
    if not account.delete_user(db,id) :
        raise HTTPException(status_code=400,detail="در حذف کاربر خطا رخ داده است")
    return BaseMessage(message="کاربر مورد نظر با موفقیت حذف شد")


@router.patch("/",status_code=200,response_model=BaseMessage)
def EditUserDetail(req:EditUserRequst, db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security)):
    user=account.get_by_id(db,req.id)
    if user is None :
        raise HTTPException(status_code=404,detail="کاربر مورد نظر یافت نشد")
    user.id=req.id
    user.fName=req.fName
    user.lName=req.lName
    user.tell=req.tell
    db.commit()
    return BaseMessage(message="اطلاعات کاربر با موفقیت ویرایش شد")

@router.patch("/",status_code=200,response_model=BaseMessage)
def EditUserDetail(req:EditUserRequst, db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security)):
    #admin
    user=account.get_by_id(db,req.id)
    if user is None :
        raise HTTPException(status_code=404,detail="کاربر مورد نظر یافت نشد")
    user.id=req.id
    user.fName=req.fName
    user.lName=req.lName
    user.tell=req.tell
    user.password=req.password
    user.reagentCode=req.reagentCode
    user.isAdmin=req.isAdmin
    db.commit()
    return BaseMessage(message="اطلاعات کاربر با موفقیت ویرایش شد")

@router.patch("/changepass",status_code=200,response_model=BaseMessage)
def changepass(req:UserPasswordChangeRequest,db:Session=Depends(get_db),credentials: JwtAuthorizationCredentials = Security(access_security)):
    user=account.get_by_id(db,req.id)
    if user is None :
        raise HTTPException(status_code=404 , detail="کاربر مورد نظر یافت نشد")
    hashed=hashlib.md5(req.password.encode('utf-8'))
    user.password=hashed.hexdigest()
    db.commit()
    return BaseMessage(message="کلمه عبور کاربر با موفقیت تغییر کرد")    
