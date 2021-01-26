"""Base settings."""
from pathlib import Path

import environ

# Environment variables
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=bool)
env.read_env(str(BASE_DIR / ".env"))

# SECRET_KEY and DEBUG are irrelevant since we're not running a web application
SECRET_KEY = "SECRET-KEY-IS-IRRELEVANT-SINCE-THERE-IS-NO-WEBSERVER"
DEBUG = True

# UML DIRECTORY
UML_EXPORTS_DIR = BASE_DIR / ".exports"
UML_EXPORTS_DIR.mkdir(exist_ok=True)


# Application definition
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    # LOCAL APPS
    "apps.commands",
    "apps.example",
    # THIRD PARTY
    "django_extensions",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "portal" / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {"default": env.db()}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Amsterdam"
USE_I18N = True
USE_L10N = True
