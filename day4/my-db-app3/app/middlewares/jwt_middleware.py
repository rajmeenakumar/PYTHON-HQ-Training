import time
import logging
from fastapi import HTTPException, Request
from app.utils.jwt_handler import verify_token

# logging.basicConfig(level=logging.INFO , filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

async def jwt_middleware(request: Request, call_next):
    print("JWt middleware called.....")
    token = request.headers.get('Authorization')
    
    if token and token.startswith('Bearer '):
        print(token)  # Remove 'Bearer ' from the token string to get the actual token)
        token = token.replace('Bearer ', '')
        payload = verify_token(token)
        if payload:
            request.state.user = payload
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    else:
        print("Missing or invalid token")
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    response = await call_next(request)
    return response