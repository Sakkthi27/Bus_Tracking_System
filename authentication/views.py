
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_str,force_bytes
from btn import settings
from . tokens import generate_token
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import reverse
import serial

# Create your views here. templates/
def index(request):
    return render(request,"authentication/index.html")



def signup(request):

    if request.method =='POST':
        fname = request.POST['fullName']
        username =request.POST['userName']
        email = request.POST['email']
        pass1 = request.POST['newPassword']
        pass2 = request.POST['conPassword']


        if User.objects.filter(username=username):
            messages.error(request,"Username already Exist! Please use another Username")
            return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request,"email already Exist! Please use another email")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request,"Your password didn't Match")
            return redirect('signup')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.save()
        messages.success(request,"Account created successfully")


        # welcome mail

        subject = "Welcome to ROUTE EXPRESS"
        message = "Hello " + fname + "\n Welcome to ROUTE EXPRESS \n your account has been successfully created. \n Thank you for Using our website"
        from_mail=settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_mail,to_list,fail_silently=True)

        return redirect('signin')


    return render(request,"authentication/signup.html")




def signin(request):

    if request.method =='POST':
        uname =request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return render(request,"authentication/index.html")

        else:
            messages.error(request,"Bad Request!")
            return redirect('index')



    return render(request,"authentication/login.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('index')


def routes(request):
    return render(request,"authentication/routes.html")

def trip_planner(request):
    return render(request,"authentication/trip_planner.html")

def stops(request):
    return render(request,"authentication/stops.html")

def favourites(request):
    return render(request,"authentication/favourites.html")

def faq(request):
    return render(request,"authentication/faq.html")

def about(request):
    return render(request,"authentication/about.html")

def contact(request):
    return render(request,"authentication/contact.html")
