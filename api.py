import requests

def fetchData(name):
    # The headers are required to authenticate the request
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzODBhNGU5OGNkMjIyZWMxMWQ1MmY5NjExOGIwZmRjZSIsInN1YiI6IjY1ZDRmZjUyNTZiOWY3MDE3Y2IyOWM2NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hCotRo8Fj6W9HOc00lI3RKVja3teyKxWGheJOg09API"
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie?query="+name+"&include_adult=true&language=en-US&page=1", headers=headers)

    data = response.json()
    # Assuming 'data' is the dictionary you posted
    results = data.get('results')
    if results:
        first_movie = results[0]
        movie_name = first_movie.get('title')
        description = first_movie.get('overview')
        poster_image = first_movie.get('poster_path')

    
    return movie_name, description, poster_image   # returns the movie name, description and poster image
    
    
