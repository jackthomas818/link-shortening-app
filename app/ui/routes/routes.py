from flask import Blueprint, render_template
from ui.ui import ui_blueprint


@ui_blueprint.route("/")
def index():
    return render_template("index.html")
