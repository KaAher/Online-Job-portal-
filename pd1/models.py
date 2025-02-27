from django.db import models

# Create your models here.
class Jobs(models.Model):
    company_name=models.CharField(max_length=500)
    job_role=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default="default@email.com")
    salary=models.IntegerField()
    description=models.CharField(max_length=10000)

class User(models.Model):
    email=models.CharField(max_length=200,default="default@email.com")
    password=models.CharField(max_length=200)
    
class Apply(models.Model):
    company_name=models.CharField(max_length=500)
    email=models.CharField(max_length=200,default="Not Specified")
    name=models.CharField(max_length=200,default="Anonymous")
    role=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    resume=models.FileField(upload_to="resumes/")

class Userjob(models.Model):
    email=models.CharField(max_length=200,default="default@email.com")
    password=models.CharField(max_length=200)











    



