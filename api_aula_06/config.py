from datetime import timedelta
DEBUG = True

USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'escola'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=30)