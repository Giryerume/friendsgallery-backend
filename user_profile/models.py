from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_data')
    day_of_birth=models.DateField(null=True,blank=True,default=None)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    profile_image=models.ImageField(upload_to="profile_image",null=True,blank=True)
