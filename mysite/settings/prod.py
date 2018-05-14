import os

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@mg.bottlenose.co'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

DATABASES = {
    'default': os.environ['DATABASE_URL'],
}