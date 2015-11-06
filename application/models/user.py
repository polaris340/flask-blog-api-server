from application import db
from .model import TimestampMixin


class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
