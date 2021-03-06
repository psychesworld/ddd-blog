from flask import Flask
from flask_migrate import Migrate

from config import config
from flask_ddd import DDD
from .common.adapter.repositories.sql import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    DDD(app)
    Migrate(app, db)

    from .blog.presentation import blog
    app.register_blueprint(blog)

    return app
