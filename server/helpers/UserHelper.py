class UserHelper:

    def __call__(self, user) -> dict:
        return { key:(value if key != "_id" else str(value)) for key, value in user.items() if key != 'password' }

    