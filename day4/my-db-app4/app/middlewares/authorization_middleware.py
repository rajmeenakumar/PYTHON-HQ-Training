from fastapi import Request, HTTPException

def authorize_role(allowed_roles: list):
    def role_checker(request: Request):
        user = getattr(request.state, "user", None)
        if not user or user['role'] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied: insufficient permissions")
    return role_checker
