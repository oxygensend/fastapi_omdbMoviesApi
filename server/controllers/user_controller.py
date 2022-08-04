from bson.objectid import ObjectId
from  ...main import app
from ..database import user_collection
from ..helpers import user_helper

@app.get('/api/users')
async def getAllUsers():
    return [ user_helper(user) async for user in user_collection.find()]