from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)

class Donor(models.Model):
    name = models.CharField(max_length=30)
    userId = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    bloodgroup = models.CharField(max_length=5)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    ldd = models.DateField()

class Organisation(models.Model):
    orgname = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    orgtype = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact = models.IntegerField()

class StateCity(models.Model):
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30,primary_key=True)

class Inbox(models.Model):
    userId = models.CharField(max_length=30,primary_key=True)
    message = models.CharField(max_length=150)