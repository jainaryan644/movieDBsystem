from flask import Blueprint, jsonify, request
from db_connection import get_db_connection

movies_blueprint = Blueprint("movies", __name__)

# Test route
@movies_blueprint.route("/")
def movies_home():
    return "Movies route works!"

# Get all movies
@movies_blueprint.route("/", methods=["GET"])
def get_all_movies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT mid, title, release_date, avg_rating FROM movie_")
    movies = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(movies)

@movies_blueprint.route("/dump", methods=["GET"])
def dump_movies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT mid, title, release_date, avg_rating FROM movie_")
    movies = cur.fetchall()
    cur.close()
    conn.close()

    # Convert each tuple to a dictionary with labels
    movies_with_labels = [
        {
            "mid": movie[0],
            "title": movie[1],
            "release_date": movie[2].strftime('%Y-%m-%d') if movie[2] else None,
            "avg_rating": movie[3]
        }
        for movie in movies
    ]

    return jsonify(movies_with_labels)

@movies_blueprint.route("/search/<movie_title>", methods=["GET"])
def search_movies(movie_title):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT mid, title, release_date, avg_rating FROM movie_ WHERE title ILIKE %(name)s LIMIT 5", dict(name='%'+movie_title.strip()+'%'))
    movies = cur.fetchall()
    cur.close()
    conn.close()

    # Convert each tuple to a dictionary with labels
    movies_with_labels = [
        {
            "mid": movie[0],
            "title": movie[1],
            "release_date": movie[2].strftime('%Y-%m-%d') if movie[2] else None,
            "avg_rating": movie[3]
        }
        for movie in movies
    ]
    return jsonify(results=movies_with_labels)


# Get movie details
@movies_blueprint.route("/<int:movie_id>", methods=["GET"])
def get_movie_details(movie_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT m.mid, m.title, m.release_date, m.plot, m.avg_rating, ARRAY_AGG(g.genre_name) AS genres
        FROM movie_ m
        LEFT JOIN genre_of_ go ON m.mid = go.mid
        LEFT JOIN genre_ g ON go.genre_name = g.genre_name
        WHERE m.mid = %s
        GROUP BY m.mid
    """, (movie_id,))
    movie = cur.fetchone()
    cur.close()
    conn.close()

    return jsonify(movie)
