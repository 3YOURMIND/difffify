import json
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=1000, primary_key=True)

    def __str__(self):
        return self.name


class FilePath(models.Model):
    path = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag, blank=True)
    additional_info_json = models.TextField(blank=True)