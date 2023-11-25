from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=255, default="Description")
    cat_img=models.ImageField(null=True,blank=True,upload_to="images/category/")
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:50px;height:50px;border-radius:50%">'.format(self.cat_img))
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    linkedin_url=models.CharField(max_length=255,null=True,blank=True)
    instagram_url=models.CharField(max_length=255,null=True,blank=True)
    twitter_url=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_img=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255)
    category=models.CharField(max_length=255,default='coding')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    #body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    snippet=models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('home')
    def total_likes(self):
        return self.likes.count()