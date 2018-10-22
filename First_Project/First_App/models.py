from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    Cus_ID=models.IntegerField(unique=True)
    Cus_Name=models.CharField(max_length=255)

class Bank(models.Model):
    Bank_ID=models.IntegerField(unique=True)
    Bank_Name=models.CharField(max_length=255,unique=True)
class Account(models.Model):
    C_ID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    B_ID=models.ForeignKey(Bank,on_delete=models.CASCADE)
    Ammount=models.IntegerField()

class SignUP(models.Model):
    Name=models.CharField(max_length=255)
    Nick_name=models.CharField(max_length=255)
    Bari=models.CharField(max_length=255)
    Mobile=models.IntegerField()
