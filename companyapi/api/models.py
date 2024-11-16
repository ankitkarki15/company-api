from django.db import models

# Create your models here.
#1 company models
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Non IT','Non IT'),
                                                  ('Mobile Phones','Mobile Phones')
                                                  )) 
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    # ('Non IT','Non IT'),=this is tuples for choice
    
    def __str__(self):
        return self.name
    
# 2 employee model
class Employee(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50) 
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about = models.TextField() 
    position=models.CharField(max_length=50,choices=(
                              ('Manager','Manager'),('Software Developer','sd'),
                              ('Project Head','ph')
                              ))
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE, default=1)
    