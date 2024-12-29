from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    E_mail=models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tags(models.Model):
    Caption= models.CharField(max_length=40)
    
    def __str__(self):
        return self.Caption
    
class Posts(models.Model):
    title= models.CharField(max_length=100)
    excerpt= models.CharField(max_length=200)
    image_name= models.CharField(max_length=100)
    date= models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,)
    content=models.TextField(validators=[MinLengthValidator(50)])
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags= models.ManyToManyField(Tags)

    def __str__(self):
        return f"{self.title} ,{self.date}"