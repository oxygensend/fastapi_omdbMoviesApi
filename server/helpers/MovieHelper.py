class MovieHelper:

    def __call__(self, movie) -> dict:
        return {
            "id": str(movie["_id"]),
            "title": movie["title"],
            "year": movie["year"],
            "released": movie["released"],
            "runtime": movie["runtime"],
            "genres": movie["genres"],
            "directors": movie["directors"],
            "actors": movie["actors"],
            "language": movie["language"],
            "country": movie["country"],
            "awards": movie["awards"],
            "metascore": movie["metascore"],
            "rating": movie["rating"],
            "votes": movie["votes"],
            "income": movie["income"]
        }

    