from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length = 255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __str__(self):
        return ("{}-{}".format(self.amount, self.date))

class Income(models.Model):
    text = models.CharField(max_length = 255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def __str__(self):
        return ("{}-{}".format(self.amount, self.date))

