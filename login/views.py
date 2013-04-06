# Create your views here.
from django.http import HttpResponse
from DNF.auth.login import Login
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
l = Login()

@csrf_exempt
def login(request):
    if not request.POST:
        return render_to_response("login.html",{'no_post':True})
    else:
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        ip_addr = str(request.META['REMOTE_ADDR'])
        
        yo = str(l.ip4(username, password, ip_addr))
        
        return redirect('loggedin/') 

def login_ok(request):
        return HttpResponse("Login ok.")