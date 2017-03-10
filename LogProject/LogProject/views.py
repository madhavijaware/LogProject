# Create your views here.
import json,datetime
from django.http import HttpResponse
from .models import *
import time
from django.http import JsonResponse
from django.shortcuts import render_to_response,render
from django.contrib import auth



#def Index_page(request):
 #       return render_to_response('html_templates/Index.html')




def user_login_page(request):
        return render_to_response('html_templates/signin.html')

def registration_page(request):
        return render_to_response('html_templates/signup.html')

def logout_page(request):
        return render_to_response('html_templates/logout.html')

def logout_page(request):
    logout(request)
    return HttpResponse('html_templates/index.html')

def home_page(request):
    return render_to_response('html_templates/index.html')

def home(request):
    return render_to_response('index.html', { 'user': request.user })    

 
def login(request):
    jsonobj=request.POST
    print jsonobj

    user_name=jsonobj.get("user_name")
    password=jsonobj.get("password")

    if user_name == None:
        return HttpResponse(json.dumps({'validation':'Enter user name' , "status": False}), content_type="application/json")
    elif password == None:
        return HttpResponse(json.dumps({'validation':'Enter password first' , "status": False}), content_type="application/json")

    user = authenticate(username=user_name,password=password)

    if not user:
        return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    if not user.is_active:
        return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

    login(request,user)
    return HttpResponse(json.dumps({'validation':'Login successfully', "status": True}), content_type="application/json")


def logout(request):
    auth.logout(request)
    return HttpResponse("/account/loggedout/")


def registration(request):
    jsonobj = request.POST
    print jsonobj
    
    #user_name=jsonobj.get("User_Name")
    u_mobno=jsonobj.get("Mobile_Number")
    u_email=jsonobj.get("Email")
    
    user = jsonobj.get('User_Name')
    user_password = jsonobj.get('User_Password')
    conform_password = jsonobj.get('Conform_Passsword')
    print user 
    
    if user == None:
       return HttpResponse(json.dumps({'validation':'name is required', 'status':False}), content_type="application/json")
    
    if not user_password == conform_password:
        return HttpResponse(json.dumps({'validation':'password not matched', 'status':False}), content_type="application/json")
    
    if User.objects.filter(username=user).exists():
        return HttpResponse(json.dumps({'validation':'username already exists', 'status':False}), content_type="application/json")
    
    
    user = User.objects.create(username=user)
    user.set_password(user_password)
    user.save()
    
    client=Client.objects.create(mob_no= u_mobno,email = u_email, user_name = user,password = user_password,confirm_pwd =conform_password)
    
    #return HttpResponse(json.dumps({'validation':'registraion succesfully', 'status':True}), content_type="application/json")
    return render_to_response("html_templates/sigin.html")

#def registration(request):
#   reg=json.loads(request.body)
#    print (reg)
#
#    uname=reg.get("Client_name")
#    umobno=reg.get("mob_no")
#    uemail=reg.get("email")
#
#    user_name = reg.get('user_name')
#    user_pswrd = reg.get('user_pswrd')
#    cnfrm_pswrd = reg.get('cnfrm_pswrd')
#
#    if (user_pswrd) < 8:
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
#    client=Client.objects.create(client_name=uname,mob_no=umobno,email=uemail,user=user)
#
#    return  HttpResponse(json.dumps({'validation':'registraion succesfully', "status":True}), content_type="application")
#
#
#
#
#
#