# Create your views here.
from django.http import HttpResponse
from DNF.auth.login import Login
from django.shortcuts import render_to_response

l = Login()

def check_login(request):
    if not request.GET:
        return HttpResponse("NO LOGIN GIVEN")
    
    username = str(request.GET['username'])
    password = str(request.GET['password'])
    ip_addr = str(request.META['REMOTE_ADDR'])
    
    return HttpResponse(str(l.ip4(username, password, ip_addr)))

def show_login(request):
        return render_to_response("login.html")