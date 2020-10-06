import os

class Config:
    pass
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brenda-wanjiku:brenda@localhost/pitch'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True 
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
} 
