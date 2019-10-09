"""
Initial Api configuration
"""
import os

class Config:
    """
    base configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """
    Testing configurations, which separate test database
    """
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL_TEST')

class StagingConfig(Config):
    """
    Staging configurations
    """
    DEVELOPMENT = True
    DEBUG = False

class ProductionConfig(Config):
    """
    Production Configuration
    """
    DEBUG = False
    TESTING = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
