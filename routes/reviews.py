from flask import Blueprint, jsonify, request
from db_connection import get_db_connection

reviews_blueprint = Blueprint("reviews", __name__)

# Test route
@reviews_blueprint.route("/")
def reviews_home():
    return "reviews route works!"

# This is a one-off to make the interface cleaner after a user has already reviewed a movie
@reviews_blueprint.route("/validate_review/<int:user_id>/<int:movie_id>") 
def check_already_reviewed(user_id, movie_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if the user has already reviewed this movie
    cur.execute("SELECT 1 FROM review_ WHERE uid = %s AND mid = %s", (user_id, movie_id))
    existing_review = cur.fetchone()

    if existing_review:
        cur.close()
        conn.close()
        return jsonify({"result": True}), 200
    return jsonify({"result": False}), 200

@reviews_blueprint.route("/add", methods=["POST"])
def add_review():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if the user has already reviewed this movie
    cur.execute("SELECT 1 FROM review_ WHERE uid = %s AND mid = %s", (data["uid"], data["mid"]))
    existing_review = cur.fetchone()

    if existing_review:
        cur.close()
        conn.close()
        return jsonify({"message": "User has already reviewed this movie!"}), 409

    # Insert the new review
    cur.execute("""
        INSERT INTO review_ (uid, mid, comment, rating, date, vote)
        VALUES (%s, %s, %s, %s, CURRENT_DATE, 0)
    """, (data["uid"], data["mid"], data["comment"], data["rating"]))

    # Update the movie's rating_sum and num_reviews
    cur.execute("""
        UPDATE movie_ 
        SET rating_sum = rating_sum + %s, num_reviews = num_reviews + 1 
        WHERE mid = %s
    """, (data["rating"], data["mid"]))

    # Fetch updated average user rating and number of reviews
    cur.execute("""
        SELECT rating_sum, num_reviews 
        FROM movie_ 
        WHERE mid = %s
    """, (data["mid"],))
    updated_movie_data = cur.fetchone()
    avg_user_rating = updated_movie_data[0] / updated_movie_data[1] if updated_movie_data[1] else 0

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "message": "Review added successfully!",
        "avg_user_rating": avg_user_rating,
        "num_user_reviews": updated_movie_data[1],
    }), 201


# Get reviews for a specific user
@reviews_blueprint.route("/user/<int:user_id>", methods=["GET"])
def get_reviews_for_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.rid, r.comment, r.rating, r.date, m.title AS movie_title
        FROM review_ r
        JOIN movie_ m ON r.mid = m.mid
        WHERE r.uid = %s
        ORDER BY r.date DESC
    """, (user_id,))
    reviews = cur.fetchall()
    cur.close()
    conn.close()

    reviews_with_labels = [
        {
            "rid": review[0],
            "comment": review[1],
            "rating": review[2],
            "date": review[3].strftime('%Y-%m-%d') if review[3] else None,
            "movie_title": review[4],
        }
        for review in reviews
    ]
    return jsonify(reviews_with_labels)


@reviews_blueprint.route("/movie/<int:movie_id>", methods=["GET"])
def get_reviews_for_movie(movie_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.rid, r.comment, r.rating, r.date, u.username
        FROM review_ r
        JOIN user_ u ON r.uid = u.uid
        WHERE r.mid = %s
        ORDER BY r.date DESC
    """, (movie_id,))
    reviews = cur.fetchall()
    cur.close()
    conn.close()

    reviews_with_labels = [
        {
            "rid": review[0],
            "comment": review[1],
            "rating": review[2],
            "date": review[3].strftime('%Y-%m-%d') if review[3] else None,
            "username": review[4],
        }
        for review in reviews
    ]
    return jsonify(reviews_with_labels)
