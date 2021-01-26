"""Default settings for running the project."""
# pylint: disable=wildcard-import,unused-wildcard-import,relative-beyond-top-level
from .base import *  # noqa

SECRET_KEY = "SECRET-KEY-IS-IRRELEVANT-SINCE-THERE-IS-NO-WEBSERVER"
DEBUG = env("DEBUG")

# DJANGO EXTENSIONS
# https://django-extensions.readthedocs.io/
INSTALLED_APPS += ["django_extensions"]

GRAPH_MODELS = {
    "all_applications": False,
    "group_models": True,
    "app_labels": ["example"],
}

UML_EXPORTS_DIR = BASE_DIR / ".exports"
UML_EXPORTS_DIR.mkdir(exist_ok=True)
