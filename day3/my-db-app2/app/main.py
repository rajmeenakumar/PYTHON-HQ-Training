from fastapi import FastAPI, HTTPException, Depends
from app.routers import destinations, category
from . import models
from . import database



app = FastAPI()

models.Base.metadata.create_all(database.engine)


app.include_router(destinations.router, prefix="/api/v1/destinations")
app.include_router(category.router, prefix="/api/v1/categories")

