from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    location = models.TextField()
    domain = models.CharField(max_length = 40 ,choices=(("IT","IT"), ("Non IT","Non IT")))
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length = 23)
    
    def __str__(self):
        return self.name
    