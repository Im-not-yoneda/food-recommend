from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food(models.Model):
    name = models.CharField('name',max_length=100)
    calorie = models.IntegerField('calorie')
    value = models.IntegerField('value')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)