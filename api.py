import requests
from creds import key

def fetchData(name):
    # The headers are required to authenticate the request
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + key()
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie?query="+name+"&include_adult=true&language=en-US&page=1", headers=headers)

    data = response.json()
    results = data.get('results')
    
    # Return the data of the first movie
    if results:
        first_movie = results[0]
        movie_name = first_movie.get('title')
        description = first_movie.get('overview')
        poster_image = first_movie.get('poster_path')
        movie_id = results[0].get('id')
          
    return movie_name, description, poster_image, movie_id   # returns the movie name, description and poster image

def fetchSimilar(id):
    # The headers are required to authenticate the request
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + key()
    }
    
    similar = requests.get("https://api.themoviedb.org/3/movie/"+ str(id) +"/recommendations", headers=headers)
    
    similar_data = similar.json()
    similar_results = similar_data.get('results')

    if similar_results:
        similar_movies = similar_results[:4]  # Get the first four similar movies
        similar_movie_data = [(movie.get('title'), movie.get('poster_path')) for movie in similar_movies]
        return similar_movie_data
    else:
        return []  # Return an empty list if no similar movies found
    
    
