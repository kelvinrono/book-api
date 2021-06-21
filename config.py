 import os

class Config:

    BOOK_API_BASE_URL =''
    BOOK_API_KEY = os.environ.get('BOOK_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}