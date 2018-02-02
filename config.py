# import os


class Config:
    """
    General parent configurations
    """
    pass
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:Sam@localhost/pitch_ip'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    """
    pass


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
