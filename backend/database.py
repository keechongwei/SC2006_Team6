from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.errors import DuplicateKeyError, OperationFailure

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def init_app(app):
    """
    Initialize the MongoDB connection with the Flask app
    """
    mongo = PyMongo(app)
    
    # Close the database connection when the request ends
    @app.teardown_appcontext
    def close_db_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            # The connection will be closed automatically by PyMongo
            pass