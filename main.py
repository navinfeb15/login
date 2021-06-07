from fastapi import FastAPI, Depends
from sqlalchemy.sql.functions import mode
import models
from database import engine
from routers import users, admin, authorization

app = FastAPI()


app.include_router(authorization.router)
app.include_router(admin.router)
app.include_router(users.router)

models.Base.metadata.create_all(engine)
