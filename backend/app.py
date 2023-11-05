from flask import Flask
from flask_cors import CORS
from api.routes import api_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
