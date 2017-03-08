# Create your views here.
import json,datetime
from django.http import HttpResponse
from .models import *
import time
from django.http import JsonResponse
from django.shortcuts import render_to_response,render
from django.contrib import auth



def Index_page(request):
        return render_to_response('html_templates/Index.html')




def user_login_page(request):
        return render_to_response('html_templates/login.html')

def registration_page(request):
        return render_to_response('html_templates/signup.html')

def logout_page(request):
        return render_to_response('html_templates/logout.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def home(request):
    return render_to_response('html_templates/home.html',{ 'user': request.user })

 
def user_login(request):
    jsonobj=request.POST
    print jsonobj

    user_name=jsonobj.get("user_name")
    password=jsonobj.get("password")

    user = auth.authenticate(username = user_name,password = password)

    if user is not None and user.is_active:
        auth.authenticate.login(request,user)
        return HttpResponse("/account/loggedin/")
    else:
        return HttpResponse("/account/ invalid/")


#def registration(request):
#    reg=json.loads(request.body)
#    print (reg)
#
#    uname=reg.get("name")
#    umobno=reg.get("contact")
#    uemail=reg.get("email")
#
#    user_name = reg.get('user_name')
#    user_pswrd = reg.get('password')
#    cnfrm_pswrd = reg.get('confirm_pwd')
#
#    if len(user_pswrd) < 8:
#        return HttpResponse(json.dumps({'validation':'please enter minimum 8 characters', "status":False}), content_type="application/json")
#
#    if not user_pswrd == cnfrm_pswrd:
#        return HttpResponse(json.dumps({'validation':'password not matched', "status":False}), content_type="application/json")
#
#    if(user_name and uname) == None:
#        return HttpResponse(json.dumps({'validation':'name is required', "status":False}), content_type="application/json")
#
#    if User.objects.filter(username=user_name).exists():
#        return HttpResponse(json.dumps({'validation':'username already exists', "status":False}), content_type="application/json")
#
#
#    user = User.objects.create(username=user_name)
#    user.set_password(user_pswrd)
#    user.save()
#
#    client=Client.objects.create(name=uname,contact=umobno,email=uemail,user=user)
#
#    return  HttpResponse(json.dumps({'validation':'registraion succesfully', "status":True}), content_type="application")
#

def logout(request):
    auth.logout(request)
    return HttpResponse("/account/loggedout/")


def registration(request):
    jsonobj = json.loads(request.body)
    print jsonobj
    
    first_name=jsonobj.get("First_Name")
    last_name=jsonobj.get("Last_Name")
    u_mobno=jsonobj.get("Mobile_Number")
    u_email=jsonobj.get("Email")
    
    user = jsonobj.get('User_Name')
    user_password = jsonobj.get('User_Password')
    conform_password = jsonobj.get('Conform_Passsword')
    print user ,first_name
    
    if(user and first_name) == None:
       return HttpResponse(json.dumps({'validation':'name is required', 'status':False}), content_type="application/json")
    
    if not user_password == conform_password:
        return HttpResponse(json.dumps({'validation':'password not matched', 'status':False}), content_type="application/json")
    
    if User.objects.filter(username=user).exists():
        return HttpResponse(json.dumps({'validation':'username already exists', 'status':False}), content_type="application/json")
    
    
    user = User.objects.create(username=user)
    user.set_password(user_password)
    user.save()
    
    client=Client.objects.create(first_name = first_name,last_name = last_name,mob_no= u_mobno,email = u_email, user=user)
    
    return HttpResponse(json.dumps({'validation':'registraion succesfully', 'status':True}), content_type="application/json")
