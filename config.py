# Enable Flask's debugging features. Should be False in production
class Config(object):
    """
    Common Configurations
    """
class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}