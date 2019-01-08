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
    DEVELOPMENT = True
    DEBUG = False
    TESTING = False

    # url = "dbname=ireporter user=bafiam_admin password=bafiam host=127.0.0.1 port=5432"


class TestingConfig(Config):
    """
        Configurations for Testing
    """
    #url = "dbname=ireporter_test user=bafiam_admin password=bafiam host=127.0.0.1 port=5432"
    TESTING = True
    DEBUG = True
    os.environ['ENV'] = 'testing'
    DATABASE_URL = os.getenv('DATABASE_URL_TEST')


class ProductionConfig(Config):
    """configuration for the production environment"""
    DEBUG = False
    TESTING = False





app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
