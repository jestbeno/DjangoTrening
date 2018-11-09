from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(default="",max_length=20)
    date_created=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(default="",max_length=20)
    paradigm = models.CharField(default="",max_length=20)
    date_created = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name
