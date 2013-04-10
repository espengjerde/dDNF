# Create your views here.
from django.http import HttpResponse
from DNF.auth.login import Login
from DNF.stats import info 
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.context_processors import csrf
l = Login()
ip = info.IP()

@csrf_exempt
def login(request):    
    ip_addr = str(request.META['REMOTE_ADDR'])
    if ip.isLoggedIn(ip_addr):
        return redirect('stats/')
    if not request.POST:
        link = "http://"+request.META.get('HTTP_HOST')+request.get_full_path()
        return render_to_response("login.html",{'no_post':False, 'link':link})
    else:
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        link = str(request.POST['link'])
            
        print(str(l.ip4(username, password, ip_addr)))
        
        return redirect(link) 
    return render_to_response("login.html",{'no_post':True})

def statistics(request):
    return HttpResponse(ip.getStats(request.META['REMOTE_ADDR']))

def checkmeta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>M: %s</td><td>%s</td></tr>' % (k, v))
    values = request.GET.items()
    values.sort()    
    for k, v in values:
        html.append('<tr><td>G: %s</td><td>%s</td></tr>' % (k, v))    
    return HttpResponse('<table>%s</table>' % '\n'.join(html))