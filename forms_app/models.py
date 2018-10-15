from django.db import models
from datetime import datetime


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.TextField(max_length=1000)
    timeCook = models.IntegerField()
    dateCreated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name