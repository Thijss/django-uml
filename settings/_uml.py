"""Setting that enable `python manage.py uml` command"""
# pylint: disable=wildcard-import, unused-wildcard-import
from ._base import *

_INSTALLED_APPS_SET = set(INSTALLED_APPS).union({
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django_extensions"
})
INSTALLED_APPS = list(_INSTALLED_APPS_SET)

UML_EXPORTS_DIR = BASE_DIR / ".exports"
UML_EXPORTS_DIR.mkdir(exist_ok=True)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]
