from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/')
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
