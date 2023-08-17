from flask import Blueprint, jsonify, request
from services.services import LinkService

link_blueprint = Blueprint("link", __name__)
link_service = LinkService()


@link_blueprint.route("/shorten", method=["POST"])
def shorten_link():
    data = request.json
    long_url = data.get("long_url")

    link = link_service.generate_shorten_url(long_url)

    response = jsonify(link.__dict__)

    return response, 201
