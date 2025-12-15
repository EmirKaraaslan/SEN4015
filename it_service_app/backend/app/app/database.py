from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config import get_settings

settings = get_settings()

# MongoDB client instance
client: AsyncIOMotorClient = None
database: AsyncIOMotorDatabase = None


async def connect_to_mongo():
    """Creates database connection at application startup."""
    global client, database
    
    client = AsyncIOMotorClient(settings.MONGO_URI)
    database = client[settings.DATABASE_NAME]
    
    # Test the connection
    try:
        await client.admin.command('ping')
        print("[OK] Successfully connected to MongoDB Atlas!")
    except Exception as e:
        print(f"[ERROR] Failed to connect to MongoDB: {e}")
        raise e


async def close_mongo_connection():
    """Closes database connection at application shutdown."""
    global client
    
    if client:
        client.close()
        print("[INFO] MongoDB connection closed.")


def get_database() -> AsyncIOMotorDatabase:
    """Returns the database instance."""
    return database
