from django.db import models

# Create your models here.
class DoctorD(models.Model):
    pfp = models.ImageField(upload_to="doctorPfp/",blank=True,null=True)
    name = models.CharField(blank=True, max_length=50)
    workCateg = models.CharField(blank=True, max_length=50)
    workExperience = models.CharField(blank=True, max_length=50)
    workSpecialization = models.CharField(blank=True, max_length=50)
    workLanguage = models.CharField(blank=True, max_length=50)
    doctorAbout = models.TextField(blank=True, max_length=1000)