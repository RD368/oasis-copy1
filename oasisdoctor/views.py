from django.shortcuts import render
from .models import DoctorD

# Create your views here.

def findDoctors(request):

    allDoctor = DoctorD.objects.all()
    print(allDoctor)

    return render(request,"findDoctor.html")