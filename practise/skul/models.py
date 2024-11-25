from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)

class Subject(models.Model):
    student = models.ForeignKey(Student, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    marks = models.IntegerField()

