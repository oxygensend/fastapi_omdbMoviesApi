import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.movies

user_collection = database.get_collection("users_collection")
movies_collection = database.get_collection("movies_collection")