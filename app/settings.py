import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_LANG = os.environ.get("APP_LANG")
LANGUAGES = ['fr']
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = ['contact@nicolaskempf.fr']
