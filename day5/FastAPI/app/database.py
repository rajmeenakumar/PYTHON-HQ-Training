from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.mongodb_url)
db = client.fastapi_db
item_collection = db.get_collection("items")
user_collection = db.get_collection("users")