from fastapi import Request, HTTPException
from app.utils.jwt_handler import verify_access_token

async def jwt_middleware(request: Request, call_next):

    public_paths = ["/auth/login", "/auth/register"]

    if request.url.path in public_paths:
        return await call_next(request)

    token = request.headers.get("Authorization")

    # if not token:
    #     raise HTTPException(status_code=401, detail="Authorization token required")

    # print(token)
    
    if token and token.startswith("Bearer "):
        token = token.split(" ")[1]
        payload = verify_access_token(token)
        if payload:
            request.state.user = payload
            
        else:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
    else:
        request.state.user = None
        raise HTTPException(status_code=401, detail="Invalid or expired token abc")

    response = await call_next(request)
    return response
    
