from fastapi import FastAPI
from api.handler import account,province,city,store,category,slider,food,menu,theme,pager


from sqlalchemy.orm import Session

from database import CRUD, models
from database.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
def create_app():
    app = FastAPI(docs_url="/api/docs")
    origins = [
    "http://localhost",
    "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=account.router)
    app.include_router(router=province.router)
    app.include_router(router=city.router)
    app.include_router(router=store.router)
    app.include_router(router=category.router)
    app.include_router(router=slider.router)
    app.include_router(router=food.router)
    app.include_router(router=menu.router)
    app.include_router(router=theme.router)
    app.include_router(router=pager.router)

    return app