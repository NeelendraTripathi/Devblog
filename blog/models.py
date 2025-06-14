from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    
    title = models.CharField(max_length=200)
    
    slug = models.SlugField(max_length=200, unique=True ,default='post_name')
    
    header_image_url =models.URLField(max_length=200 , null= True , blank=True)
    
    
    content = models.TextField()
    
    author = models.ForeignKey(User , on_delete= models.CASCADE) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
    
   
    
    