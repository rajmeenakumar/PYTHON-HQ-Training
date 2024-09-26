import time
import logging
from fastapi import HTTPException, Request
from app.utils.jwt_handler import verify_token

# logging.basicConfig(level=logging.INFO , filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

async def jwt_middleware(request: Request, call_next):

    public_paths = ["/api/v1/auth/login", "/api/v1/auth/register", "/api/v1/categories/", "/docs","/openapi.json", "/api/v1/categories" ]

    if request.url.path in public_paths:
        return await call_next(request)

    token = request.headers.get("Authorization")

    # if not token:
    #     raise HTTPException(status_code=401, detail="Authorization token required")

    # print(token)
    
    if token and token.startswith("Bearer "):
        token = token.split(" ")[1]
        payload = verify_token(token)
        if payload:
            request.state.user = payload
            
        else:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
    else:
        request.state.user = None
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    response = await call_next(request)
    return response