import os

class Config:

    BOOK_API_BASE_URL ='https://api.nytimes.com/svc/books/v3/lists/{}/hardcover-fiction.json?api-key={}'
    BOOK_API_KEY = os.environ.get('BOOK_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = ''


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}