class UserHelper:

    def __call__(self, user) -> dict:
        return {
            "id": str(user["_id"]),
            "fullname": user["username"],
            "email": user["email"],
        }

    