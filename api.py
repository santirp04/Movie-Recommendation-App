import requests
from creds import key

def fetchData(name):
    # The headers are required to authenticate the request
    creds = ...  # Define the variable "creds" with the appropriate value
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + key()
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
    
    
