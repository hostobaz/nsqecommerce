# modules
from django.db import models

class Schools(models.Model):
    name = models.CharField(max_length=20)
    max_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name