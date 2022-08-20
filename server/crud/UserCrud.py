import imp
from bson import ObjectId
from .CrudInterface import CrudInterface
from ..helpers.UserHelper import UserHelper
from ..database import user_collection
from ..filters.UserFilter import UserFilter

class UserCrud(CrudInterface):

    userHelper = UserHelper()

    @classmethod
    async def retriveAll(cls, params) ->dict:

        if params:
           filter = UserFilter()
           query, fields =  filter.build(params)
        else:
            query, fields = None, None


        return [ cls.userHelper(user) async for user in user_collection.find(query, fields)]

    @classmethod
    async def retriveOne(cls, id: str, params) -> dict:
        
        if params:
           filter = UserFilter()
           _ , fields =  filter.build(params)
        else:
            fields = None

        user = await user_collection.find_one({"_id": ObjectId(id)})
        return cls.userHelper(user) if user else None

    @classmethod
    async def add(cls, data: dict) ->dict:
        user = await user_collection.insert_one(data)
        new_user = await user_collection.find_one({"_id": user.inserted_id})
        return cls.userHelper(new_user)

    @classmethod
    async def update(cls, id: str,  data: dict) -> bool:
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
