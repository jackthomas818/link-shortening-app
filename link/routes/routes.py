from link.controllers.controllers import shorten_link
from flask import Blueprint

link_blueprint = Blueprint("link", __name__)

link_blueprint.add_url_rule("/shorten", view_func=shorten_link, methods=["POST"])
