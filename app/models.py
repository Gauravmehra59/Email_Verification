import email
from operator import mod
from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50,default=False)
    email = models.EmailField()
    password = models.CharField(max_length=50,default=False)

class token_verify(models.Model):
    user_id = models.ForeignKey(Signup,on_delete=models.CASCADE, default=False, primary_key=True)
    tokken = models.CharField(max_length=150,default=False)
    verify = models.BooleanField(default=False)    
