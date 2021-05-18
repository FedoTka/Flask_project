class Configuration(object):
    Debug=True
    SECRET_KEY='3143247d'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1111@localhost/test2'


    ###Flask-security
    SECURITY_PASSWORD_SALT='salt'
    SECURITY_PASSWORD_HASH='sha512_crypt'