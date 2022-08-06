class Response:

    @classmethod
    def json(cls,data, code=200):
        return {
            "data": [data],
            "code": code,
        }


    @classmethod
    def error(cls,error,  message, code):
        return {
            "error": error,
            "message": message,
            "code": code 
        }
