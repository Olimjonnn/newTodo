from django.db import models


class Works(models.Model):
    name = models.CharField(max_length=300)
    day = models.DateField()
    finished = models.BooleanField(default=False)
    views = models.IntegerField(default=0)