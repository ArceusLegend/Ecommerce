"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY_D", "")

# SECURITY WARNING: don't run with debug turned on in production!
# False by default, change it in .env
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Must have a valid value if DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "cart",
    "users",
    "payment",
    "orders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processor.categories",
                "cart.context_processor.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "sqlite3").lower()  # Supports 'sqlite3', 'postgres' and mysql

if DATABASE_ENGINE == "sqlite3":
    DATABASE_LOCATION = os.getenv("DB_LOCATION", "db.sqlite3")  # Always relative to project dir
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / DATABASE_LOCATION,
        }
    }

elif DATABASE_ENGINE == "postgres":
    DB_SERVER = os.getenv("DB_SERVER", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "postdb")
    DB_USER = os.getenv("DB_USERNAME", "admin")
    DB_PASS = os.getenv("DB_PASSWORD", "1q2w3e4r")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": DB_SERVER,
            "PORT": DB_PORT,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASS,
        }
    }

elif DATABASE_ENGINE == "mysql":
    DB_SERVER = os.getenv("DB_SERVER", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "mysqldb")
    DB_USER = os.getenv("DB_USERNAME", "admin")
    DB_PASS = os.getenv("DB_PASSWORD", "1q2w3e4r")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": DB_SERVER,
            "PORT": DB_PORT,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASS,
        }
    }

else:
    raise ImproperlyConfigured("Unknown database engine '{!s}'".format(DATABASE_ENGINE))

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "EET"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "assets/")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Cart session ID
CART_SESSION_ID = "cart"

# Custom user model
AUTH_USER_MODEL = "users.UserBase"
LOGIN_REDIRECT_URL = "/users/dashboard"
LOGIN_URL = "/users/login/"

# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe payment
PUBLISHABLE_KEY = os.getenv("PUBLISHABLE_KEY")
SECRET_KEY = os.getenv("SECRET_KEY_S")
STRIPE_ENDPOINT_SECRET = os.getenv("STRIPE_ENDPOINT_SECRET")
# stripe listen --forward-to localhost:8000/payment/webhook/
