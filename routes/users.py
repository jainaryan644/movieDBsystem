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
@users_blueprint.route("/update", methods=["POST"])
def update_user_info():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    match data["element"]:
        case "bio":
            cur.execute("UPDATE user_ SET bio = %s WHERE uid = %s", (data["bio"],data["uid"]))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"message": "User bio updated successfully!"}), 201
        case "password":
            pt_nPassword = data["nPassword"]
            nPassword_hash = hashlib.sha256(pt_nPassword.encode()).hexdigest()
            pt_cPassword = data["cPassword"]
            cPassword_hash = hashlib.sha256(pt_cPassword.encode()).hexdigest()
            cur.execute("SELECT hash FROM user_ WHERE uid = %s", (data["uid"],))
            currentHash = cur.fetchone()[0]
            print(cPassword_hash)
            print(pt_cPassword)
            print(currentHash)
            if(cPassword_hash != currentHash): return jsonify({"message": "Invalid credentials"}), 401
            cur.execute("UPDATE user_ SET hash = %s WHERE uid = %s", (nPassword_hash, data["uid"]))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"message": "User password updated successfully!"}), 201
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Invalid element selected"}), 401
    
    
    


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
    cur.execute("SELECT uid, username, bio FROM user_ WHERE uid = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({
            "uid": user[0],
            "username": user[1],
            "bio": user[2]
        })
    else:
        return jsonify({"message": "User not found"}), 404

