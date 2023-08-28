from config import Config
from extensions import db
from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name=Config):
    app = Flask(__name__)

    # Load the configuration based on the provided config_name
    app.config.from_object(config_name)

    # Initialize extensions with the app
    db.init_app(app)

    # Import and register blueprints here
    from link.routes.routes import link_blueprint
    from ui.routes.routes import ui_blueprint

    app.register_blueprint(link_blueprint, url_prefix="/link")
    app.register_blueprint(ui_blueprint, url_prefix="/ui")

    # Configure allowed origins in production environment.
    CORS(app)

    # Redirect root URL to /ui
    @app.route("/")
    def root():
        return redirect(url_for("ui.index"))

    return app
