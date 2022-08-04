from asyncio.windows_events import NULL
from bson import ObjectId
import CrudInterface
from ..helpers import user_helper
from ..database import user_collection

class UserCrud(CrudInterface):

    @classmethod
    async def retriveAll(cls) ->dict:
        return [ user_helper(user) async for user in user_collection.find()]

    @classmethod
    async def retriveOne(cls, id: str) -> dict:
        user = await user_collection.find_one({"_id": ObjectId(id)})
        return user_helper(user) if user else None

    @classmethod
    async def add(cls, data: dict) ->dict:
        user = await user_collection.insert_one(data)
        new_user = await user_collection.find_one({"_id": user.inserted_id})
        return user_helper(new_user)

    @classmethod
    async def update(cls, data: dict) -> bool:
        if len(data) < 1:
            return False
        user = await user_collection.find_one({"_id": ObjectId(id)})
        if user:
            updated_user = await user_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            return True if updated_user else False
        return False

    @classmethod
    async def delete(cls, id: str) -> bool:
        user = await user_collection.find_one({"_id": ObjectId(id)})
        if user:
            await user_collection.delete_one({"_id": ObjectId(id)})
            return True
        else:
            return False
