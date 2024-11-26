from flask import Blueprint, jsonify, request
from db_connection import get_db_connection
import hashlib

users_blueprint = Blueprint("users", __name__)

# Register a new user
@users_blueprint.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
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

# Authenticate a user
@users_blueprint.route("/login", methods=["POST"])
def login_user():
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
