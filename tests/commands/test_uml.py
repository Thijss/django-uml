"""This module contains tests for management commands in the commands app"""

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase

from apps.commands.management.commands.uml import UML_FILE_NAME


class TestUML(TestCase):
    """Test the `python manage.py uml` command."""

    def test_smoke_uml(self):
        """Smoke test for the command"""
        settings.UML_EXPORTS_DIR = settings.BASE_DIR / "tests"

        uml_file_path = settings.UML_EXPORTS_DIR / UML_FILE_NAME

        call_command("uml")
        self.assertTrue(uml_file_path.exists())
        uml_file_path.unlink()
