from flask import Flask
from api.routes import api_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
