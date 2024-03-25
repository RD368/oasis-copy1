from django.shortcuts import render,redirect
from oasisauth.models import CustomUser,PatientRecord
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def  register(request):
    if request.method=="POST":
        email = request.POST['email']
        username = request.POST['fullname']
        password = request.POST['password']
        cPassword = request.POST['cPassword']
        sex = request.POST['sex']
        age = request.POST['age']
        phoneNumber = request.POST['phoneNumber']
        # Checking the fields are empty or not
        if not username or not email or not password or not cPassword:
            return render(request,"oasisauth/register.html",{"error":"All fields must be filled"})
        
        #Checking Password and Confirm Password field matches
        if password != cPassword:
            return render(request,'oasisauth/register.html',{'error':'Passwords do not match'})
        else:
            user = CustomUser.objects.create_user(email = email,password = password,fullName=username,sex=sex,age=age,phoneNumber = phoneNumber)
            user.save()
            try:
                return redirect('/auth/login')
            except Exception as e:
                print(e)

    return render(request, 'oasisauth/register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            print("none")
            return render(request,"oasisauth/login.html",{"msg":"Invalid Username or Password"})
        else:
            login(request,user)
            return redirect('/')


    return render(request,'oasisauth/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def  patientDashboard(request):
    if request.user.is_authenticated:
        patient = PatientRecord.objects.get(patient=request.user)
        context = {'patient': patient} 
        return render(request,'oasisauth/patientDashboard.html',context)
    else:
        return redirect('login')
    