from flask import Flask
from flask_cors import CORS
from routes.routes import link_blueprint

app = Flask(__name__)
app.register_blueprint(link_blueprint, url_prefix="/link")

# Configure allowed origins in production environment.
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
