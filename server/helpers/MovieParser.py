from datetime import date, datetime
import re
import string

from pip import main


class MovieParser:

    @classmethod
    def parse(cls, movie) -> dict:
        
        movie = {key: cls.checkIfNotNA(field) for key, field in movie.items()}

        runtime = int(movie['Runtime'].split()[0] or 0)
        rating  = float(movie['imdbRating'] or 0)
        votes = int(movie['imdbVotes'].replace(',','') or 0)
        income = float( re.sub(r'[$,]', '', movie['BoxOffice'])) if 'BoxOffice' in movie else None 
        released = datetime.strptime(movie['Released'], "%d %b %Y")
        metascore = float(movie['Metascore'] or 0) 

    
        return {
            "title": movie["Title"],
            "year": movie["Year"],
            "released": released,
            "runtime": runtime,
            "genres": movie["Genre"],
            "directors": movie["Director"],
            "actors": movie["Actors"],
            "language": movie["Language"],
            "country": movie["Country"],
            "awards": movie["Awards"],
            "metascore": metascore,
            "rating": rating,
            "votes": votes,
            "income": income
        }

    @classmethod
    def checkIfNotNA(cls, field):
        return field if field != 'N/A' else None