from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

# class Category_group(models.Model):
    # name_skill = models.CharField(max_length=100)

    # def __str__(self) -> str:
        # return self.name_skill


class Post(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    # category_name = models.ForeignKey(Category_group, on_delete=models.CASCADE, default=True)

    skill = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

     