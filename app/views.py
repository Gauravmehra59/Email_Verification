import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from requests import request
from .models import Signup
from app.models import token_verify
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def send__mail(email,token):
    subject = "Verify"
    message = f"Hi Click on the link to verify your account http://127.0.0.1:8000/account-verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

def home(request):
    return render(request,'app/home.html')

class login(View):
    def get(self,request):

        return render(request,'app/login.html')
    
    def post(self,request):
        email = request.POST.get("email",False)
        password = request.POST.get("psw",False)

        user = Signup.objects.get(email=email )
        token = token_verify.objects.get(user_id=user)
        print(token.verify)
        if user.password == password:
            if token.verify == True:
                msg = user.name
                return render(request,'app/home.html',{"msg":msg})
            else:
                messages.error(request,"Please Verify the email ")
                return redirect('/login/')
        else:
            messages.error(request,"Password Invalid")
            return redirect('/login/')
            

class Signupview(View):
    def get(self,request):
        return render(request,'app/register.html')
    
    def post(self,request):
        name = request.POST.get("name",False)
        email = request.POST.get("email",False)
        psw = request.POST.get("psw",False)
        re_psw =request.POST.get("psw-repeat",False)
        uid = uuid.uuid4()
        user = Signup.objects.filter(email=email)
        if user:
            messages.error(request,"Email already exist")
            return redirect('/signup/')
            
        else:
            if psw == re_psw:
                user_insert = Signup.objects.create(name=name,
                                                email=email,
                                                password=psw)


                user_token = token_verify.objects.create(user_id=user_insert ,tokken=uid) 
                send__mail(email,uid)
                messages.success(request,"Your Account created sucessfully, to verify your account check your email")
                return redirect('/signup/')
            else:
                messages.error(request,"Password is not same")
                return redirect('/signup/')
            


def account_verify(request,token):
    user = token_verify.objects.filter(tokken=token).first()
    user.verify = True
    user.save()
    messages.info(request,"Verify Sucessfully")
    return redirect('/signup/')
