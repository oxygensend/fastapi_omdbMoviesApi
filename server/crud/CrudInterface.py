from pydantic import BaseModel


class CrudInterface:

    @classmethod
    async def retriveAll(cls) ->dict:
        """Get whole collection from database"""
        pass

    @classmethod
    async def retriveOne(cls, id: str) -> dict:
        """Get one object from database"""
    

    @classmethod
    async def add(cls, data: dict) ->dict:
        """Add object to database"""
        pass

    @classmethod
    async def update(cls, data: dict) -> dict:
        """Pass updated object to database"""
        pass

    @classmethod
    async def delete(cls, id: str) -> dict:
        """Delete object from database"""
        pass

    
