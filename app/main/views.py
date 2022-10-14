from . import main


@main.route("/")
def index():
    return "Le blueprint waka"
