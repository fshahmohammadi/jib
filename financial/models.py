from django.db import models

# Create your models here.

class User(models.Model):
    username= models.CharField(max_length=30)
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    
    
class Golden(models.Model):
    user= models.ForeignKey(User)
    account= models.IntegerField()
    
class Transaction(models.Model):
    ttype= models.CharField(max_length=20)
    amount= models.IntegerField()
    date= models.DateField()
    user= models.ForeignKey(User)
    
class Balance(models.Model):
    amount= models.IntegerField()
    user= models.ForeignKey(User)
    date= models.DateField()