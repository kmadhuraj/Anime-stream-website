from django.db import models

# Create your models here.
class Homepagecontent(models.Model):
    main_heading=models.CharField(max_length=100),
    sub_text=models.TextField(),
    background_img=models.ImageField(upload_to='images')
    
class Signups(models.Model):
    first_name=models.CharField(max_length=50,default='default_value')
    second_name=models.CharField(max_length=50,default='default_value')
    email=models.EmailField(max_length=50,default='default_value')
    password=models.CharField(max_length=50)
    cpass=models.CharField(max_length=50,default='default_value')
    
    def __str__(self):
        return self.first_name

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    Video=models.FileField(upload_to='vdeo')
    image=models.ImageField(upload_to='img')
    title=models.CharField(max_length=200)
    desc=models.TextField()
    type=models.CharField(max_length=50)
    release_date=models.DateField()
    genre=models.TextField()
    country=models.CharField(max_length=50)
    score=models.DecimalField(max_digits=3,decimal_places=2)
    duration=models.CharField(max_length=20) 
    episodes=models.IntegerField()
    
    def __str__(self):
        return self.title
    