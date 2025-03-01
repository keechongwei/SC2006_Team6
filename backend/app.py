import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_cors import CORS
from routes.auth import auth_bp
from routes.institutions import institutions_bp
from routes.test_mongo_routes import test_mongo_bp, init_mongo as init_test_mongo
from routes.user_routes import user_bp, init_mongo as init_user_mongo
import database

load_dotenv()

app = Flask(__name__)
CORS(app)

# Get MongoDB credentials from environment variables
username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")

mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.nl9y4.mongodb.net/SC2006_api_db?retryWrites=true&w=majority&appName=Cluster0"

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)

init_test_mongo(mongo)
init_user_mongo(mongo)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(institutions_bp)
app.register_blueprint(test_mongo_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
