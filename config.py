import os

class Config:

    BOOK_API_BASE_URL ='https://api.nytimes.com/svc/books/v3/lists/{}/hardcover-fiction.json?api-key={}'
    BOOK_API_KEY = os.environ.get('BOOK_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = ''
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kelvin@localhost/book'
 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


>>>>>>> c53debbc4d04ce128ef7cfa2543841917b3687ef
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}