from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
# Create your models here.


class Customer1(models.Model ):
    cusID = models.IntegerField()
    cusName = models.CharField( max_length= 30)
    curPhoneNumber = models.IntegerField(max_length=10)

class Customer2(models.Model):
    cusName = models.CharField(max_length=30)
    curPhoneNumber = models.IntegerField(max_length=10)
    cusBirthday = models.DateField()
    cusAddress  = models.CharField (max_length= 100)

class Athlete(models.Model):
    athleteTeam = models.CharField(max_length=20)
    athleteID = models.ForeignKey(Customer1, on_delete=models.CASCADE)

class Member(models.Model):
    memberID = models.ForeignKey(Customer1, on_delete=models.CASCADE)
    memberRenewalTime = models.DateField()
    memberType = models.CharField(max_length=30) #eventually mabe a value from a list?
