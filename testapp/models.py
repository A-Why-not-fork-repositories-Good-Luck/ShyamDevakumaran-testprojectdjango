from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# class Contact(models.Model):
#     id = models.Field(null=True)
#     fName = models.CharField(max_length=50)
#     lName = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     gender = models.CharField(max_length=10)
#     date = models.DateField()
#     phone = models.IntegerField(unique=True)
#     message = models.CharField(max_length=500)

class Student(models.Model):
    id_rollno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    batch = models.IntegerField()

def __str__(self):
    return self.id_rollno

class Marks(models.Model):
    id_rollno = models.ManyToManyField(Student)
    tamil = models.IntegerField()
    english = models.IntegerField()
    computer = models.IntegerField()
    maths = models.IntegerField()

class Contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=300)

class Customer(models.Model):
    cus_id=models.AutoField(primary_key=True)
    cus_name=models.CharField(max_length=20)
    cus_email=models.EmailField()
 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cus_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def _str_(self):
        return self.cus_name