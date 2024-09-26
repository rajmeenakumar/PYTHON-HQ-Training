from fastapi import FastAPI, HTTPException, Depends
from app.routers import destinations, category, auth
from . import models
from . import database
from app.middlewares.logging_middleware import logging_middleware

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.middleware("http")(logging_middleware)  # This middleware is applied to all routes
# app.middleware("http")(logging_middleware)
# app.middleware("http")(middleware2)


app.include_router(destinations.router, prefix="/api/v1/destinations")
app.include_router(category.router, prefix="/api/v1/categories")
app.include_router(auth.router, prefix="/api/v1/auth")

