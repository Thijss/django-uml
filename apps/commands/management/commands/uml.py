"""This module stores the manage.py uml command."""
from django.core.management import BaseCommand, call_command
from django.conf import settings

UML_FILE_NAME = "UML.png"


class Command(BaseCommand):
    """This command generates a UML diagram in .png format."""

    help = "Creates UML diagram"

    def handle(self, *args, **options):
        uml_path = settings.UML_EXPORTS_DIR / UML_FILE_NAME
        call_command(
            "graph_models",
            all_applications=True,
            exclude_models="ContentType",
            output=f"{uml_path}",
        )
        self.stdout.write(self.style.SUCCESS(f"Created {uml_path}"))
