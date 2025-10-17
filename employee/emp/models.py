from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    email=models.EmailField()
    ph=models.IntegerField()
    designation=models.CharField(max_length=20)
    salary=models.IntegerField()
    image=models.ImageField(upload_to="images")