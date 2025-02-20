from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.institutions import institutions_bp
import db

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(institutions_bp)

if __name__ == '__main__':
    app.run(debug=True)
