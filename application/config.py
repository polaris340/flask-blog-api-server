import os
basedir = os.path.abspath(os.path.dirname(__file__))

is_local = not os.environ.get('SECRET_KEY')
DATABASE_URI = 'mysql+pymysql://root@localhost/blogdb'
if not is_local:
    # TODO: 서버 디비 설정
    pass

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vb252@fh!fvvR63Anj9j0r9npRb5X8b4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = is_local
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_BINDS = {
        'view': SQLALCHEMY_DATABASE_URI
    }

    @classmethod
    def init_app(cls, app):
        app.config.from_object(cls)
