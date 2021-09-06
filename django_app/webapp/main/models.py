from django.db import models

# Create your models here.
class TestUser(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
