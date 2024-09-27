from fastapi import FastAPI
from app.routers import items, users, auth
import uvicorn

app = FastAPI()

# Include the routers
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
