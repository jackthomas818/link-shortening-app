from flask import Blueprint, render_template

ui_blueprint = Blueprint(
    "ui",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@ui_blueprint.route("/")
def index():
    return render_template("index.html")
