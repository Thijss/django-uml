"""This module contains tests for management commands in the commands app"""
from django.core.management import call_command
from django.test import TestCase


class TestUML(TestCase):
    """Test the `python manage.py uml` command."""

    def test_smoke_uml(self):
        call_command("uml")
