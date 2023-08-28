from flask import Flask
import pytest
from link.controllers.controllers import link_blueprint
from extensions import db
from config import Config


@pytest.fixture
def app():
    app = Flask(__name__)
    # Load the configuration based on the provided config_name
    app.config.from_object(Config)
    app.register_blueprint(link_blueprint, url_prefix="/")
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_shorten_link(client):
    # Simulate an HTTP POST request
    data = {"long_url": "https://www.example.com"}
    response = client.post("/shorten/", json=data)

    assert response.status_code == 201
    assert "short_url" in response.json


def test_shorten_link_missing(client):
    # Simulate an HTTP POST request
    data = {"long_url": ""}

    response = client.post("/shorten/", json=data)

    assert response.status_code == 400
