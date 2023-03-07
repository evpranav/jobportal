from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class index2model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class profilepost(models.Model):
    catchoice = [
        ('remote', 'remote'),
        ('hybrid', 'hybrid'),
    ]
    jobtype = [
        ('parttime', 'parttime'),
        ('fulltime', 'fulltime'),
    ]
    exp = [
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3-4', '3-4'),
        ('4-5', '4-5'),
    ]
    username=models.CharField(max_length=20)
    email=models.EmailField()
    jobtitle=models.CharField(max_length=20)
    worktype=models.CharField(max_length=20,choices=catchoice)
    experiencerequired=models.CharField(max_length=20,choices=exp)
    jobtype=models.CharField(max_length=20,choices=jobtype)



class regmodel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    dob = models.DateField()
    qualification = models.CharField(max_length=25)
    phoneno = models.IntegerField()
    password = models.CharField(max_length=20)


class applyjobmodel1(models.Model):
    qualification=models.CharField(max_length=20)
    phone=models.IntegerField()
    exp=models.IntegerField()
    resume=models.FileField()
