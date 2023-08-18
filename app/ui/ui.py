from flask import Blueprint


ui_blueprint = Blueprint(
    "ui",
    __name__,
    template_folder="templates",
    static_folder="static",
)
