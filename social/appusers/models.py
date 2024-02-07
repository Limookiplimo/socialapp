from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/',null=True,blank=True)
    realname = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique=True,null=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    