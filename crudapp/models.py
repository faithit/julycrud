from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    def __str__(self):
        return f'Name:{self.fullname}, Age:{self.age},course:{self.course}'