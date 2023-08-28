from flask import Flask
import pytest
from link.controllers.controllers import link_blueprint
from extensions import db
from config import Config
from link.services.services import LinkService


def test_generate_short_url():
    app = Flask(__name__)

    # Load the configuration based on the provided config_name
    app.config.from_object(Config)

    # Database initialization
    from link.models.models import Link

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        link_service = LinkService()
        long_url = "https://www.example.com/some/long/url"

        link = link_service.generate_shorten_url(long_url)

    assert link.id
    assert link.long_url == long_url
    assert link.short_url.startswith("http://localhost:5000/")
