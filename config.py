import os


class Config:
    """
    General parent configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:Sam@localhost/pitch_ip'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLE_USE_CDN = True

    @staticmethod
    def init_app(app):
        app


class ProdConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # pass


class TestConfig(Config):
    """
    Child configurations with the Config passed in as a class.

    To test out database relationship.
    """
    pass


class DevConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
