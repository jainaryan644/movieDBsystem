from flask import Flask, jsonify
from flask_cors import CORS
from routes.movies import movies_blueprint
from routes.reviews import reviews_blueprint
from routes.users import users_blueprint

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(movies_blueprint, url_prefix="/movies")
app.register_blueprint(reviews_blueprint, url_prefix="/reviews")
app.register_blueprint(users_blueprint, url_prefix="/users")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Movie Review App!"})

if __name__ == "__main__":
    app.run(debug=True)
