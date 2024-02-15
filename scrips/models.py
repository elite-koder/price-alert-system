from django.db import models

# Create your models here.

class Scrip(models.Model):
    code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)