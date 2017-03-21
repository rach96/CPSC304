from django.db import connection
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User

# Create your models here.


# class Customer1(models.Model ):
#     cusID = models.IntegerField(primary_key=True)
#     cusName = models.CharField( max_length= 30)
#     cusPhoneNumber = models.IntegerField(max_length=10)
#
# class Customer2(models.Model):
#     cusName = models.CharField(max_length=30, primary_key=True)
#     cusPhoneNumber = models.IntegerField(max_length=10, primary_key=True)
#     cusBirthday = models.DateField()
#     cusAddress  = models.CharField (max_length= 100)
#
# class Athlete(models.Model):
#     athleteTeam = models.CharField(max_length=20)
#     athleteID = models.ForeignKey(Customer1, on_delete=models.CASCADE, primary_key=True)
#
# class Member(models.Model):
#     memberID = models.ForeignKey(Customer1, on_delete=models.CASCADE, primary_key=True)
#     memberRenewalTime = models.DateField()
#     memberType = models.CharField(max_length=30) #eventually mabe a value from a list?
#
# class Equipment_checkIn_reserveOrcancel_return1(models.Model):
#     EquipType = models.CharField(max_length=20, primary_key=True)
#     EquipRate = models.FloatField
#     EquipDamageFee = models.FloatField()
#
# class Equipment_checkIn_reserveOrcancel_return2(models.Model):
#     EquipID = models.IntegerField(primary_key=True)
#     EquipType = models.CharField(max_length=20)
#     EquipCustID = models.ForeignKey(Customer1, on_delete=models.CASCADE)