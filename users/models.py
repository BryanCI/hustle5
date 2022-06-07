from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # this will tell django how to print out the profile
    def __str__(self) -> str:
        return f'{self.user.username} profile'

    # resizing the uploaded profile picture to 300 by 300 pixels we override the save function
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) 
            img.save(self.image.path) # we resave it to the same path to override the initial image 
            
