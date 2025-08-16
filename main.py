from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies = {
    1: {
        "title": "Inception",
        "genre": "Sci-fi",
        "watched": False,
        "ratings": []
    }
}

# (Rest of your API continues here...)


class Movie(BaseModel):
    title: str
    genre: str
    watched: bool = False

class UpdateMovie(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    watched: Optional[bool] = None
    ratings: Optional[list[int]] = None

@app.get("/get-movie/{movie_id}")
def get_movie(movie_id: int = Path(..., description="Movie ID to view", gt=0)):
    if movie_id not in movies:
        return {"Error": "Movie not found"}
    return movies[movie_id]

@app.get("/get-movie-by-name")
def get_movie_by_name(name: Optional[str] = None):
    for mid, data in movies.items():
        if data["title"].lower() == name.lower():
            return data
    return {"Error": "Movie not found"}

@app.post("/add-movie/{movie_id}")
def add_movie(movie_id: int, movie: Movie):
    if movie_id in movies:
        return {"Error": "Movie already exists"}
    movies[movie_id] = movie.model_dump()
    movies[movie_id]["ratings"] = [] 
    return movies[movie_id]

@app.put("/update-movie/{movie_id}")
def update_movie(movie_id: int, movie: UpdateMovie):
    if movie_id not in movies:
        return {"Error": "Movie does not exist"}

    if movie.title is not None:
        movies[movie_id]["title"] = movie.title
    if movie.genre is not None:
        movies[movie_id]["genre"] = movie.genre
    if movie.watched is not None:
        movies[movie_id]["watched"] = movie.watched
    if movie.ratings is not None:
        movies[movie_id]["ratings"] = movie.ratings

    return movies[movie_id]

@app.delete("/delete-movie/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id not in movies:
        return {"Error": "Movie does not exist"}
    del movies[movie_id]
    return {"message": "Movie deleted successfully"}

@app.put("/rate-movie/{movie_id}") 
def rate_movie(movie_id: int, rating: int):
    if movie_id not in movies:
        return {"Error": "Movie not found"}
    if rating < 1 or rating > 5:
        return {"Error": "Rating must be between 1 and 5"}
    movies[movie_id]["ratings"].append(rating)
    ratings_list = movies[movie_id]["ratings"]
    avg_rating = sum(ratings_list) / len(ratings_list)
    return {"movie": movies[movie_id], "average_rating": avg_rating}
