from django.db import models

# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    E_mail=models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name},{self.E_mail}"
    

class Caption(models.Model):
    text= models.CharField(max_length=40)
    
    def __str__(self):
        return self.text
    
class Posts(models.Model):
    title= models.CharField(max_length=100)
    excerpt= models.CharField(max_length=200)
    image_name= models.CharField(max_length=100)
    date= models.DateField(auto_created=True)
    slug=models.SlugField()
    content=models.TextField(max_length=500)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.title} ,{self.date}"