from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Golden(models.Model):
    user= models.ForeignKey(User)
    account= models.IntegerField()
    def __unicode__(self):
        return self.user.name
    
class Transaction(models.Model):
    ttype= models.CharField(max_length=20)
    amount= models.IntegerField()
    date= models.DateField()
    user= models.ForeignKey(User)
    
class Balance(models.Model):
    amount= models.IntegerField()
    user= models.ForeignKey(User)
    date= models.DateField()
