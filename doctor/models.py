from django.db import models

from django.contrib.auth.models import User

from paitent.models import Paitent

# Create your models here.


class Designation(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name


class AvailableTime(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField()
    designation = models.ForeignKey(Designation,on_delete=models.SET_NULL, null = True)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.DecimalField(max_digits=10,decimal_places=2)
    meet_link=models.TextField()

    def __str__(self):
        return f'Dr. {self.user.first_name} {self.user.last_name} - {self.designation}'


rating_choices = (
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
)

class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    paitent = models.ForeignKey(Paitent, on_delete=models.CASCADE, related_name='reviews')
    rate = models.CharField(choices=rating_choices,max_length=5)
    review = models.TextField()

    def __str__(self):
        return f'{self.paitent} - {self.doctor} - {self.review}'
