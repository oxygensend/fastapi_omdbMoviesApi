class MovieHelper:

    def __call__(self, movie) -> dict:
        
        return { key:(value if key != "_id" else str(value)) for key, value in movie.items() }


    