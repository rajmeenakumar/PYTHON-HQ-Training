from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routers import destinations, category
from . import models
from . import database

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(database.engine)


app.include_router(destinations.router, prefix="/api/v1/destinations")
app.include_router(category.router, prefix="/api/v1/categories")

