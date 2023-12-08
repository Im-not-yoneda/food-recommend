from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()
    value = models.IntegerField()