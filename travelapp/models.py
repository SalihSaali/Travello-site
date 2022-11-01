from django.db import models

# Create your models here
class place (models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default='false')

class country (models.Model):
    name=models.CharField(max_length=100)
    cont=models.TextField()
    date=models.IntegerField()
    month=models.TextField()
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()