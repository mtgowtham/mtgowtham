from django.shortcuts import render, redirect
from .import models
# Create your views here.
def index(request):
    return render(request,'BikeRentalApp/index.html')
def registration(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['emailid']
        password=request.POST['password']
        userprofile=models.UserProfile (username=name,emailid=email,password=password)
        userprofile.save()

        return redirect('loginpage')
    else:
        return render(request, 'BikeRentalApp/registration.html')


def loginpage(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        UserProfile=models.UserProfile.objects.filter(emailid=email,password=password).values()
        if UserProfile==None:
            return render(request,'BikeRentalApp/login.html')
        else:
            context={'email':email}
            return render(request,'BikeRentalApp/index.html',context=context)
    else:
        return render(request,'BikeRentalApp/login.html')



def payment(request):
    return render(request,'BikeRentalApp/payment.html')

def about(request):
    return render(request,'BikeRentalApp/about.html')

def Bikes(request):
    return render(request,'BikeRentalApp/Bikes.html')

def contact(request):
    return render(request,'BikeRentalApp/contact.html')


