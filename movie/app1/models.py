from django.db import models

# Create your models here.
class Moviedetail(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    language=models.CharField(max_length=50)
    year=models.IntegerField()
    director=models.CharField()
    image=models.ImageField(upload_to="images")