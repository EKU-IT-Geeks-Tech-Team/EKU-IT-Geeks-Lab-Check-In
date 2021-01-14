from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libs
db = SQLAlchemy()


'''
this is called an app factory.
    its purpose is to allow the different components of the app to talk with the app object, without creating circular imports.

it's kinda confusing and i don't fully understand it, but this is the code for it.

before, we were just defining a global app object using:
    app = Flask(__name__)

now we have stored this functionality in a function
'''


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config

    '''
    CONFIG

    select desired enviornment using an env variable:
    export FLASK_ENV="development"

    NOTE: Env variables last until the shell is closed
    '''
    # Using a production configuration
    app.config.from_object('config.ProductionConfig')

    # Using a development configuration
    app.config.from_object('config.DevelopmentConfig')

    # init plugins
    db.init_app(app)

    with app.app_context():
        # include routes
        from .routes.main import main

        # register blueprints
        app.register_blueprint(main, url_prefix="/")

        return app
