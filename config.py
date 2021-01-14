import os


class Config:
    # BASE CONFIG
    SECRET_KEY = os.getenv("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


'''
Here we can extend the base Config class to define seperate "Production" and "Development" configs, allowing us to easily test using a local sqlite database, but use a full blown sql server in prod.
'''


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    FLASK_ENV = "production"

    # DATABASE
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = "development"

    # DATABASE
    DB_FILENAME = "test.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_FILENAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
