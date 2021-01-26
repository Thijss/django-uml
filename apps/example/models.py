"""Stores example models"""

from django.db import models


class Employer(models.Model):
    """Employer"""

    name = models.CharField(max_length=20)


class Employee(models.Model):
    """Employee"""

    name = models.CharField(max_length=20)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
