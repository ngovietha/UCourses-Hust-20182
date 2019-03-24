from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    sdt = models.IntegerField()
    email = models.EmailField()
    passwd = models.CharField(max_length=255)
    def __str__(self):
        return self.email