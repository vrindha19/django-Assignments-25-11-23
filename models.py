from django.db import models

class person(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  place = models.CharField(max_length=255)
