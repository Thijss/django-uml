"""Django settings for project."""
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
from ._uml import *  # noqa
GRAPH_MODELS = {
    "all_applications": False,
    "group_models": True,
    "app_labels": ["example"],
}
