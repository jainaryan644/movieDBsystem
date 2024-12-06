from flask import Blueprint, jsonify, request
from db_connection import get_db_connection
import hashlib

users_blueprint = Blueprint("users", __name__)

# Test route
@users_blueprint.route("/")
def users_home():
    return "users route works!"

# Register a new user
@users_blueprint.route("/register", methods=["POST"])
def register_user():
    

    data = request.get_json()
    cur.execute("SELECT 1 FROM user_ WHERE username = %s", (data["username"],)) # Check if username already in use
    existing_user = cur.fetchone()
    if(existing_user):
        cur.close()
        conn.close()
        return jsonify({"message": "Username already in use!"}), 409
    password_hash = hashlib.sha256(data["password"].encode()).hexdigest()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO user_ (username, hash, join_date, bio)
        VALUES (%s, %s, CURRENT_DATE, %s)
    """, (data["username"], password_hash, data["bio"]))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 201

# Update User Info
@users_blueprint.route("/update", methods=[])

# Authenticate a user
@users_blueprint.route("/login", methods=["POST", "GET"])
def login_user():
    if request.method == "OPTIONS":
        # Handle preflight request
        return jsonify({"message": "Preflight request successful"}), 200
    data = request.get_json()
    password_hash = hashlib.sha256(data["password"].encode()).hexdigest()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT uid FROM user_ WHERE username = %s AND hash = %s", (data["username"], password_hash))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({"uid": user[0]})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@users_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user_details(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username, bio FROM user_ WHERE uid = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({
            "username": user[0],
            "bio": user[1]
        })
    else:
        return jsonify({"message": "User not found"}), 404

