from django.db import models
import financial
# Create your models here.

class Group(models.Model):
    name= models.CharField(max_length=30)
    admin= models.ForeignKey(financial.models.Golden, related_name='golden_admin')
    users= models.ManyToManyField(financial.models.Golden, related_name='golden_users')
    def __unicode__(self):
        return self.name
    
class GroupTrans(models.Model):
    ttype= models.CharField(max_length=20)
    amount= models.IntegerField()
    user= models.ForeignKey(financial.models.Golden, related_name='golden_user')
    date= models.DateField()
    group= models.ForeignKey(Group)
    
class GroupBalance(models.Model):
    amount= models.IntegerField()
    group= models.ForeignKey(Group)
    date= models.DateField()
    
