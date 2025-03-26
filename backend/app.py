import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.institutions import institutions_bp
from routes.hawker_centres_routes import hawker_bp
from routes.login import login_bp, init_mongo as init_login_mongo
from routes.location_router import location_bp
from routes.Institution_routes import institution_bp, init_mongo as init_institution_mongo
from database import init_mongo as init_db_mongo
from database import init_db

load_dotenv()

app = Flask(__name__)
CORS(app)

# Get MongoDB credentials from environment variables
username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")

mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.nl9y4.mongodb.net/SC2006_api_db?retryWrites=true&w=majority&appName=Cluster0"

app.config["MONGO_URI"] = mongo_uri
app.config["JWT_SECRET_KEY"] = "SC2006"  # Replace with a strong key
mongo = PyMongo(app)
jwt = JWTManager(app)
# Get MongoDB collections
init_login_mongo(mongo)
init_db_mongo(mongo)
init_institution_mongo(mongo)

#Initialise Database
db = init_db()

# Register Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(institutions_bp)
app.register_blueprint(hawker_bp)
app.register_blueprint(location_bp)
app.register_blueprint(institution_bp)

if __name__ == '__main__':
    app.run(debug=True)
