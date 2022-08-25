# fastapi_omdbMoviesApi
### Authorization
Ustaw nagłowek `X-Authorization` w celu weryfikacji

schemat filtrów { pole: przykladowa wartosc}

### Movies

#### GET /api/movies
     Input: -
     Output: list of movies
     Fields: { 
            "title",
            "year",
            "released", 
            "runtime",
            "genres", 
            "directors", 
            "actors",
            "language",
            "country", 
            "awards", 
            "metascore",
            "rating",
            "votes",
            "income"}
    Query filters variables: {
        title=Titanic,
        year=2000,
        language=german,polish,
        genres=drama,comedy,
        directors=Jon B, Jon C,
        runtime_lt=10
        runtime_gt=100,
        votes_lt=1000,
        votes_gt=1000,
        rating_lt=2,
        rating_gt=10,
        metascore_lt=100,
        metascore_gt=60,
        income_lt=10000,
        income_gt=10000
        }
    Choose fields: add variable `fields` to query eg. fields=title,year,language

#### POST /api/movies
    Input: { 
        title: "Movie", - required
        year: 2001  - optional
    }
    Output: new created movie with all fields
    
    Autorization required!

#### GET /api/movies/:id
    Input: - 
    Output: movie with given id
    Query filters variables: {
    title=Titanic,
    year=2000,
    language=german,polish,
    genres=drama,comedy,
    directors=Jon B, Jon C,
    runtime_lt=10
    runtime_gt=100,
    votes_lt=1000,
    votes_gt=1000,
    rating_lt=2,
    rating_gt=10,
    metascore_lt=100,
    metascore_gt=60,
    income_lt=10000,
    income_gt=10000
    } 
    Choose fields: add variable `fields` to query eg. fields=title,year,language

#### DELETE /api/movies/:id
    Input: -
    Output: deleted movie
    
    Authorization and authentication(ADMIN ROLE) required!

#### POST /api/movies/stats
    INPUT: {
        fields: [], - required
        methods: [], - required
    }
    Ouput: calculated statistics
    Avaliable methods: {
        mean, median, mode, std, quantile
    }

### Auth

#### POST /api/auth
    Input: {
        email: "test@test.com", - required
        password: "Test123!"  - required 
    }
    Output: Auth token

### Users

#### GET /api/users
    Input: -
    Output: list of registrated users
    Fields: {
        username,
        email,
        isAdmin
        }
    Choose fields: add variable `fields` to query eg. fields=username,email
    Query filters variables: {
        username=Test,
        email=test@test.com,
        admin=1
    } 
    Authorization and authentication(ADMIN ROLE) required!
#### POST /api/users
    Input: {
        username: "Test", - required
        email: "test@test.com" - required 
        password: "Test123!" - required 
    }
    Output: username and email 
