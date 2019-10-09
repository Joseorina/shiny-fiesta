"""
Initial Api configuration
"""
import os

class Config():
    pass

class DevelopmentConfig():
    pass

class TestingConfig():
    pass

class StagingConfig():
    pass

class ProductionConfig():
    pass

APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}