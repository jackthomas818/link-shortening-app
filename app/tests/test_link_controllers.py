from flask import Flask
import pytest
from link.controllers.controllers import link_blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(link_blueprint, url_prefix="/link")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_shorten_link(client):
    # Simulate an HTTP POST request
    data = {"long_url": "https://www.example.com"}
    response = client.post("/link/shorten", json=data)

    assert response.status_code == 201
    assert "short_url" in response.json


def test_shorten_link_missing(client):
    # Simulate an HTTP POST request
    data = {"long_url": ""}

    response = client.post("/link/shorten", json=data)

    assert response.status_code == 400
