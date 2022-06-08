"""Django settings for project."""
# pylint: disable=wildcard-import, unused-wildcard-import
from ._base import *


INSTALLED_APPS += [
    "apps.commands",
    "apps.example",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

TIME_ZONE = "Europe/Amsterdam"

# UML
# pylint: disable=wrong-import-position
from ._uml import *  # noqa

GRAPH_MODELS = {
    "all_applications": False,
    "group_models": True,
    "app_labels": ["example"],
}
