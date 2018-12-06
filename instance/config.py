import os

class Config(object):
    """
        Parent configuration class.
    """
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """
        Configurations for Development.
    """
    DEBUG = True
    os.environ['ENV'] = 'development'

class TestingConfig(Config):
    """
        Configurations for Testing
    """
    TESTING = True
    DEBUG = True
    os.environ['ENV'] = 'testing'

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}