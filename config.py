# config.py


class Config(object):
    """
    Common configurations
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    DEBUG = True
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/testdb"


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
