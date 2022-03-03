from django.db import models

# Create your models here.
class User(models.Model):
    Firstname=models.CharField(max_length=15,blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    password=models.CharField(max_length=30,blank=False)
    confirmpassword=models.CharField(max_length=20,blank=False)
    Email=models.EmailField(max_length=20,blank=False)

    class Meta:
        db_table="user_table"