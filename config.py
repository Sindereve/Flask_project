import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I_am_overlord_app'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    POSTS_PER_PAGE = 10
    
    LANGUAGES = ['en', 'ru']
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'app/static/images')  
    UPLOADED_PHOTOS_ALLOW = ['jpg', 'jpeg', 'png', 'gif']

    # параметры для отправки инфо об ошибке на email
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email']
