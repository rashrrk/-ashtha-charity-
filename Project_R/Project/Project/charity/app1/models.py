from django.db import models
from django.contrib.auth.models import User
from cProfile import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

class registeredUser(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,primary_key=True)
    email=models.EmailField()
    phone_number = models.CharField(max_length=12)
    password=models.CharField(max_length=20)


freqChoice=((1,'Monthly'),(2,'One-Time'))
categoryChoice=((1,'Charity'),(2,'Campaign'))
dtype=((1,'cloth'),(2,'food'),(3,'money'))

class donateTbl(models.Model):
    username=models.ForeignKey(registeredUser,on_delete=models.CASCADE)    
    freq=models.IntegerField(choices=freqChoice)
    dtype=models.IntegerField(default=False)
    category=models.IntegerField(choices=categoryChoice)
    amount=models.DecimalField(max_digits=8,decimal_places=2,null=True)


catChoice=((1,'cancer awareness campaign'),(2,'fundraise campaign'),(3,'pulse polio campaign'),(4,'annual health care campaign'))
class campaignTbl(models.Model):
    username=models.ForeignKey(registeredUser,on_delete=models.CASCADE)    
    email=models.EmailField()
    category=models.IntegerField(choices=catChoice)
    
    

class fundraiseTbl(models.Model):
    username=models.ForeignKey(registeredUser,on_delete=models.CASCADE) 
    email=models.EmailField()
    freq=models.IntegerField(choices=freqChoice)
    category=models.IntegerField(choices=categoryChoice)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    
class volunteertbl(models.Model):
    username=models.ForeignKey(registeredUser,on_delete=models.CASCADE) 
    email=models.EmailField()
    freq=models.IntegerField(choices=freqChoice)
    category=models.CharField(max_length=50)
    
class messagetbl(models.Model):
    username=models.ForeignKey(registeredUser,on_delete=models.CASCADE) 
    email=models.EmailField()
    message=models.TextField(max_length=100)
    
    

    



    
    
   