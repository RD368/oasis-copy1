from django.shortcuts import render
from oasisauth.models import CustomUser
from django.contrib.auth import login,logout

# Create your views here.
def  register(request):
    if request.method=="POST":
        username = request.POST['fullName']
        email = request.POST['email']
        password = request.POST['password']
        cPassword = request.POST['cPAssword']
        sex = request.POST['sex']
        age = request['age']
        phoneNumber = request.POST['phoneNumber']
        # Checking the fields are empty or not
        if not username or not email or not password or not cPassword:
            return render(request,"oasisauth/register.html",{"error":"All fields must be filled"})
        
        #Checking Password and Confirm Password field matches
        if password != cPassword:
            return render(request,'oasisauth/register.html',{'error':'Passwords do not match'})
        else:
            user = CustomUser(email = email,password = password,fullName=username,sex=sex,age=age,phoneNumber = phoneNumber)
            user.save()
            try:
                pass
            except Exception as e:
                print(e)

    return render(request, 'oasisauth/register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = CustomUser.objects.filter(email=email,password=password).first()
        if user is None:
            return render(request,"oasisauth/login.html",{"msg":"Invalid Username or Password"})
        else:
            login(request,user)
            return render(request,"index.html")


    return render(request,'oasisauth/login.html')