from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, max_length=255, default="Docker")
    slug = models.SlugField(blank=False, max_length=255, default="docker")

    def __str__(self):
        return (self.name)

