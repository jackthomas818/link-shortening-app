from link.controllers.controllers import redirect_link, shorten_link
from link.link import link_blueprint

link_blueprint.add_url_rule("/shorten/", view_func=shorten_link, methods=["POST"])
link_blueprint.add_url_rule("/<code>", view_func=redirect_link, methods=["GET"])
