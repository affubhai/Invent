from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    company_name = models.CharField(max_length=100, null=True)
    item_code = models.IntegerField(null=True)

class legger(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    item_code = models.IntegerField()
    company_name = models.CharField(max_length=100, null=True)
    