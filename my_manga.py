from flask_migrate import Migrate

from app import create_app
from app import db
from app.models import Manga, Page

app = create_app("dev")
migrate = Migrate(app, db)


@app.shell_context_processor
def create_shell():
    return dict(db=db, Manga=Manga, Page=Page)
