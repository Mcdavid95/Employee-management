# Enable Flask's debugging features. Should be False in production
class Config(object):
    """
    Common Configurations
    """
    DEBUG = True
class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Test configurations
    """

    TESTING = True

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}