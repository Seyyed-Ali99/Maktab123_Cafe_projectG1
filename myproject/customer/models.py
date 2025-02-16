from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Customers(models.Model):
    ROLE_CHOICES =[
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null= True)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    password = models.CharField(max_length=128)
    birth_date = models.DateField(null = True, blank= True)
    role = models.CharField(max_length= 10, choices= ROLE_CHOICES, default= 'customer' )
    
class Message(models.Model):
    description = models.TextField()
    user = models.ForeignKey(Customers, on_delete= models.CASCADE)