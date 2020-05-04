class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ms:New Password@localhost/USER'

     
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")