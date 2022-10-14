from flask import render_template

from app.models import Manga
from . import main


@main.route("/")
def index():
    mangas = Manga.query.all()
    return render_template("index.html", mangas=mangas)
