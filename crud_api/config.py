DEBUG = True

USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'escola'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
