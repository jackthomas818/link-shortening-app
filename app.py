from flask import Flask
from flask_cors import CORS
from link.routes.routes import link_blueprint
from ui.views import ui_blueprint

app = Flask(__name__)
app.register_blueprint(link_blueprint, url_prefix="/link")
app.register_blueprint(ui_blueprint, url_prefix="/")

# Configure allowed origins in production environment.
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
