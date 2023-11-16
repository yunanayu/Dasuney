import json
import requests
import pprint

# i = 1
# url = f'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page={i}'

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjZlYjQ3Yjg1YzNhMjBlM2ZiOGE4OWZiNDNkZDA5MSIsInN1YiI6IjY1M2Y2MmNiMTA5Y2QwMDBhZDYzOGI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8yLdir57DDw30YVy__5P-tkrBicDzN0cf1_LMO0quVY"
# }

# response = requests.get(url, headers=headers).json()

# pprint.pprint(response['results'])

movies = []
genres = [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 16, "name": "Animation"}, {"id": 35, "name": "Comedy"}, {"id": 80, "name": "Crime"}, {"id": 99, "name": "Documentary"}, {"id": 18, "name": "Drama"}, {"id": 10751, "name": "Family"}, {"id": 14, "name": "Fantasy"}, {"id": 36, "name": "History"}, {
    "id": 27, "name": "Horror"}, {"id": 10402, "name": "Music"}, {"id": 9648, "name": "Mystery"}, {"id": 10749, "name": "Romance"}, {"id": 878, "name": "Science Fiction"}, {"id": 10770, "name": "TV Movie"}, {"id": 53, "name": "Thriller"}, {"id": 10752, "name": "War"}, {"id": 37, "name": "Western"}]

# for genre in genres:
#     temp = {}
#     temp['model'] = 'movies.genre'
#     temp['pk'] = genre['id']
#     fields = {}
#     fields['name'] = genre['name']
#     temp['fields'] = fields
#     movies.append(temp)

# with open('genre.json', 'w', encoding="UTF-8") as make_file:
#     json.dump(movies, make_file, indent='\t', ensure_ascii=False)

for i in range(1, 20):
    url = f'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page={i}'

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjZlYjQ3Yjg1YzNhMjBlM2ZiOGE4OWZiNDNkZDA5MSIsInN1YiI6IjY1M2Y2MmNiMTA5Y2QwMDBhZDYzOGI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8yLdir57DDw30YVy__5P-tkrBicDzN0cf1_LMO0quVY"
    }
    data = requests.get(url, headers=headers).json()
    data_result = data['results']
    for result in data_result:
        temp = {}
        temp['model'] = 'movies.movie'
        field = {}
        movie_field = ['title', 'release_date', 'popularity', 'vote_count',
                       'vote_average', 'overview', 'poster_path', 'genre_ids']

        for key, value in result.items():
            if key in movie_field and key == 'genre_ids':
                field['genres'] = value
            elif key in movie_field and key == 'poster_path':
                field['poster_path'] = f'https://image.tmdb.org/t/p/w500/{value}'
            elif key in movie_field:
                field[key] = value

        temp['fields'] = field
        movies.append(temp)

with open('movies.json', 'w', encoding="UTF-8") as make_file:
    json.dump(movies, make_file, indent='\t', ensure_ascii=False)