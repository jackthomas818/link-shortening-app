from link.controllers.controllers import shorten_link
from link.link import link_blueprint

link_blueprint.add_url_rule("/shorten", view_func=shorten_link, methods=["POST"])
