class Config:
    SECRETE_KEY= 'B!1w8NAt1T^%kvhafafUI*S^'
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'namastebd'

config={'development': DevelopmentConfig}
