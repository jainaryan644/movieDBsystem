from flask import Blueprint, jsonify, request
from db_connection import get_db_connection

movies_blueprint = Blueprint("movies", __name__)

# Test route
@movies_blueprint.route("/")
def movies_home():
    return "Movies route works!"

# Helper function for dumping movies
def dump_movies(top=False):
    conn = get_db_connection()
    cur = conn.cursor()

    if not top:
        cur.execute("SELECT mid, title, release_date, rating_sum, num_reviews FROM movie_")
    else:
        cur.execute("""
            SELECT mid, title, release_date, rating_sum, NULLIF(num_reviews, 0)
            FROM movie_
            ORDER BY rating_sum / NULLIF(num_reviews, 0) * 1.0 DESC
            LIMIT 5
        """)  # Using NULLIF to avoid division by zero

    movies = cur.fetchall()
    cur.close()
    conn.close()

    # Convert each tuple to a dictionary with labels
    movies_with_labels = []
    for movie in movies:
        avg_rating = movie[3] / movie[4] if movie[4] else 0
        movies_with_labels.append({
            "mid": movie[0],
            "title": movie[1],
            "release_date": movie[2].strftime('%Y-%m-%d') if movie[2] else None,
            "avg_rating": avg_rating,
        })

    return jsonify(movies_with_labels)

# Get all movies
@movies_blueprint.route("/", methods=["GET"])
def get_all_movies():
    return dump_movies(top=False)

# Get top movies
@movies_blueprint.route("/top", methods=["GET"])
def top_movies():
    return dump_movies(top=True)

# Search movies by title
@movies_blueprint.route("/search/<movie_title>", methods=["GET"])
def search_movies(movie_title):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT mid, title, release_date
        FROM movie_
        WHERE title ILIKE %(name)s
        LIMIT 5
    """, {"name": f"%{movie_title.strip()}%"})
    movies = cur.fetchall()
    cur.close()
    conn.close()

    # Convert each tuple to a dictionary with labels
    movies_with_labels = [
        {
            "mid": movie[0],
            "title": movie[1],
            "release_date": movie[2].strftime('%Y-%m-%d') if movie[2] else None,
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
        SELECT m.mid, m.title, m.release_date, m.plot, m.rating_sum, NULLIF(m.num_reviews, 0), ARRAY_AGG(g.genre_name) AS genres
        FROM movie_ m
        LEFT JOIN genre_of_ go ON m.mid = go.mid
        LEFT JOIN genre_ g ON go.genre_name = g.genre_name
        WHERE m.mid = %s
        GROUP BY m.mid
    """, (movie_id,))
    movie = cur.fetchone()
    cur.close()
    conn.close()

    if not movie:
        return jsonify({"message": "Movie not found"}), 404

    # Compute average rating safely
    avg_rating = round(movie[4] / movie[5],2) if movie[5] else 0

    output_movie = {
        "mid": movie[0],
        "title": movie[1],
        "release_date": movie[2].strftime('%Y-%m-%d') if movie[2] else None,
        "plot": movie[3],
        "avg_rating": avg_rating,
        "genres": movie[6] if movie[6] else [],
    }

    return jsonify(output_movie)
