from django.db import models

# Create your models here.
class Numbers(models.Model):
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='Pratik',editable=True)
    lname =  models.CharField(max_length=200, default='Pratik',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)
    
class Emergency(models.Model):
    title = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)
   
class Manchar(models.Model):
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname =  models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)