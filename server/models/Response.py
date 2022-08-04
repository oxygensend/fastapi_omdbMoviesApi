class Response:

    @classmethod
    def json(cls,data, code=200):
        return {
            "data": [data],
            "code": code,
        }


    @classmethod
    def error(cls,error, code, message):
        return {"error": error, "code": code, "message": message}
