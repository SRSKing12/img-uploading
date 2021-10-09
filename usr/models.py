from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_Name=models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    # email = models.EmailField(max_length=100, unique=True)
    state=models.CharField(max_length=60)#choices=STATE_CHOICES,default='none'
    address = models.CharField(max_length=200)
    # username = models.CharField(max_length=30, unique=True)
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.full_Name

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)