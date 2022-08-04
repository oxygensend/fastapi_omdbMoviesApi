def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["username"],
        "email": user["email"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"],
    }