import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@mg.bottlenose.co'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}