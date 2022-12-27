class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'rs2-dal.serverhostgroup.com'
    MYSQL_USER = 'cuidemos_prueba'
    MYSQL_PASSWORD = 'Acws2022*'
    MYSQL_DB = 'cuidemos_fidelizacion'


config = {
    'development': DevelopmentConfig
}
