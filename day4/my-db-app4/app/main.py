from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import auth, category, destination
from app.database import Base, engine
from app.middlewares.jwt_middleware import jwt_middleware
from app.middlewares.authorization_middleware import authorize_role
from app.middlewares.logging_middleware import logging_middleware


app = FastAPI()

Base.metadata.create_all(bind=engine)


# Middleware Registration
app.middleware("http")(logging_middleware)
app.middleware("http")(jwt_middleware)

# Routes Registration
app.include_router(auth.router, prefix="/auth")
app.include_router(category.router, prefix="/categories")
app.include_router(destination.router, prefix="/destinations")

# Custom error handler
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