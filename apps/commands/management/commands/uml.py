"""This module stores the manage.py uml command."""
from django.core.management import BaseCommand, call_command
from django.conf import settings


class Command(BaseCommand):
    """This command generates a UML diagram in .png format."""

    help = "Creates UML diagram"

    def handle(self, *args, **options):
        call_command(
            "graph_models",
            all_applications=True,
            exclude_models="ContentType",
            output=f"{settings.UML_EXPORTS_DIR / 'UML.png'}",
        )
