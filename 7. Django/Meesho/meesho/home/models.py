from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=15)
    user_email = models.EmailField(max_length=25)
    user_display_name = models.CharField(max_length=15)
    user_contact = models.CharField(max_length=15)
    user_city = models.CharField(max_length=15)
    user_date_of_birth = models.DateField()
    user_password = models.CharField(max_length=10)
    user_image = models.ImageField(upload_to='image/profile_picture')
    user_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name