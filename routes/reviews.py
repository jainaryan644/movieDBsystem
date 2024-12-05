from flask import Blueprint, jsonify, request
from db_connection import get_db_connection

reviews_blueprint = Blueprint("reviews", __name__)

# Test route
@reviews_blueprint.route("/")
def reviews_home():
    return "reviews route works!"

# Add a new review
@reviews_blueprint.route("/add", methods=["POST"])
def add_review():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO review_ (uid, mid, comment, rating, date, vote)
        VALUES (%s, %s, %s, %s, CURRENT_DATE, 0)
    """, (data["uid"], data["mid"], data["comment"], data["rating"]))
    cur.execute("UPDATE movie_ SET rating_sum = rating_sum + %s, num_rating = num_rating + 1 WHERE mid = %s", (data["rating"], data["mid"]))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Review added successfully!"}), 201

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
