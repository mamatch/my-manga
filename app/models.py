from . import db


class Manga(db.Model):
    """
    A class to represents the manga
    """
    __tablename__ = "mangas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author = db.Column(db.String(64))
    creation_date = db.Column(db.DateTime)
    cover_image_path = db.Column(db.String(200))
    pages = db.relationship("Page", backref="manga", lazy=True)


class Page(db.Model):
    """
    A class to represent a page of a manga
    """
    __tablename__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    image_path = db.Column(db.String(200))
    manga_id = db.Column(db.Integer, db.ForeignKey("mangas.id"))
