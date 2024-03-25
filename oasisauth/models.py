from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser , PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email field must be set'))
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields['is_active']=True

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        

        return self.create_user(email, password, **extra_fields)

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    fullName = models.CharField(max_length=128,blank = True)
    sex = models.CharField(max_length=128,blank = True)
    age = models.CharField(max_length=128,blank = True)
    phoneNumber = models.IntegerField(blank=True)

    # Add more fields as needed

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','fullName','sex','age','phoneNumber']

    def __str__(self):
        return self.email
    

class PatientRecord(models.Model):
    patient = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    dob = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=500, blank=True,null=True)
    bloodGroup = models.CharField(max_length=30, blank=True,null=True)
    height = models.FloatField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    bmi = models.FloatField(blank=True,null=True)
    pfp = models.FileField(upload_to= "pfp/", blank=True,null=True)
    pdf_files = models.ManyToManyField('PdfFiles',related_name="patient_records",blank=True,null=True)

    def __str__(self):
        return f"Patient record for {self.patient}"
    

class PdfFiles(models.Model):
    file = models.FileField(upload_to='pdf_files/')
    uploadedAt = models.DateTimeField(auto_now_add=True)
    