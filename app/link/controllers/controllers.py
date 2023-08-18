from flask import Blueprint, jsonify, request

from link.link import link_blueprint
from link.services.services import LinkService

link_service = LinkService()


@link_blueprint.route("/shorten", methods=["POST"])
def shorten_link():
    data = request.json
    long_url = data.get("long_url")

    link = link_service.generate_shorten_url(long_url)

    response = jsonify(link.__dict__)

    return response, 201
