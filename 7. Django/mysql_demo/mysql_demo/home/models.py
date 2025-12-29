from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    display_name = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=20)