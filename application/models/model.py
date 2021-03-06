from application import db


class TimestampMixin:
    created = db.Column(db.TIMESTAMP,
                        default=db.func.utc_timestamp())
    modified = db.Column(db.TIMESTAMP,
                         default=db.func.utc_timestamp(),
                         onupdate=db.func.utc_timestamp())

