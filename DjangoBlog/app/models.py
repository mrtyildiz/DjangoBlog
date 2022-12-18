from django.db import models
from enum import unique
from operator import mod
from django.db.models.fields import CharField
from django.conf import settings
from mdeditor.fields import MDTextField

class Socials(models.Model):
    SocialsName = models.CharField(max_length=25)
    SocialsURL = models.URLField(max_length = 200)
    def __str__(self):
        return self.SocialsName

class About(models.Model):
    AboutName = models.CharField(max_length=255)
    P1 = models.CharField(max_length=255)
    Header= models.CharField(max_length=255)
    P2 = models.CharField(max_length=255)
    Profil_Image = models.ImageField(upload_to='images')
    body = MDTextField(null=True, blank=True)
    def __str__(self):
        return self.AboutName

class Topics(models.Model):
    TopicsName = models.CharField(max_length=50)
    def __str__(self):
        return self.TopicsName

class Blog(models.Model):
    filter = models.ForeignKey(Topics, on_delete=models.CASCADE)
    HeaderImage = models.ImageField(upload_to='Blog')
    HeaderName = models.CharField(max_length=25)
    body = MDTextField(null=True, blank=True)
    def __str__(self):
        return self.HeaderName
