from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=50)
    sbranch=models.CharField(max_length=50)
    smob=models.IntegerField()
    bookname=models.CharField(max_length=50)
    bookno=models.IntegerField()

# Create your models here.
