# from django.db import models
from djongo import models

class Example(models.Model):
name = models.CharField(max_length=255, blank=False)
value = models.FloatField()
date_created = models.DateTimeField(auto_now_add=True)
date_modified = models.DateTimeField(auto_now=True)

