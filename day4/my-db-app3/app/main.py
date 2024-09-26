from fastapi import FastAPI, HTTPException, Depends, Request
from app.routers import destinations, category, auth
from . import models
from . import database
from app.middlewares.logging_middleware import logging_middleware
from app.middlewares.jwt_middleware import jwt_middleware
from fastapi.responses import JSONResponse

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.middleware("http")(logging_middleware)  # This middleware is applied to all routes
app.middleware("http")(jwt_middleware)  # This middleware is applied to all routes
# app.middleware("http")(middleware2)


app.include_router(destinations.router, prefix="/api/v1/destinations")
app.include_router(category.router, prefix="/api/v1/categories")
app.include_router(auth.router, prefix="/api/v1/auth")

@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    # print(exc.status_code)
    if exc.status_code:
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": str(exc)},
        )
    return JSONResponse(
        status_code= 500,
        content={"message": "An unexpected error occurred", "details": str(exc)},
    )