from django.db import models
from random import randint
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length =255)
    date = models.DateField()
    des = models.CharField(max_length =255)
    num = models.IntegerField(default = randint(0,50) )
    view = models.IntegerField(default= randint(0,100) )
    def __str__(self):
        return self.name