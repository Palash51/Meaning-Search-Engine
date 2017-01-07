from __future__ import unicode_literals

from django.db import models

# Create your models here.
class words(models.Model):
    words_searched = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=30)
