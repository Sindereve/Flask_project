from flask import Flask, request, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_babel import Babel
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import logging
from logging.handlers import RotatingFileHandler  # ,SMTPHandler (добавить, если будем использовать уведомления по email)


def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return 'en'


app = Flask(__name__)
app.config.from_object(Config)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
upload_folder = app.config['UPLOADED_PHOTOS_DEST']
os.makedirs(upload_folder, exist_ok=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
babel = Babel(app, locale_selector=get_locale)

from app.api import bp as api_bp
from app.errors import register_error_handlers
register_error_handlers(app, api_bp)
app.register_blueprint(api_bp, url_prefix='/api')


@app.context_processor
def inject_view_args():
    return {
        'view_args': request.view_args if request else {}
    }


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/my_flask.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('My_flask startup')
# ========================================================================================================
#     Тут мы можем настроить отправку инфу об ошибке на почту с помощью яндекс почты
#     больше инфы тут https://yandex.ru/support/yandex-360/customers/mail/ru/mail-clients/others.html
#     Мы в россии, а что в рунете всегда стабильно
#     работа яндекс почты... Да..Да....
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr=app.config['MAIL_USERNAME'],
#             toaddrs=app.config['ADMINS'], subject='Flask Proj Failure',
#             credentials=auth, secure=secure
#         )
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)
# ========================================================================================================



from app import routes, models, errors