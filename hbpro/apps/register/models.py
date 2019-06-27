from django.db import models
#from django import forms

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, blank='False', null='False')
    password = models.CharField(max_length=100, blank='False')
    age = models.IntegerField()
    e_mail = models.CharField(max_length=50, blank='False')
    number_phone = models.IntegerField(blank='False', null='True')
    github = models.CharField(max_length=50)
    is_working = models.BooleanField(default=True)
    #subject_student = models.ManyToManyField(Subject)

    def __str__(self):
        return (self.name)
