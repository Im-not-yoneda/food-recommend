from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField('name',max_length=100)
    calorie = models.IntegerField('calorie')
    value = models.IntegerField('value')