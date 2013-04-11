# Create your views here.
from django.http import HttpResponse
from DNF.stats.info import Statistics 
from django.shortcuts import render_to_response, redirect

stats = Statistics()


def user_stats(request):
    
    ipaddr = request.META['REMOTE_ADDR'];
#    conn = stats.get_active_connections(ipaddr)
    conn = stats.get_conntrack(ipaddr)
       
    io = stats.get_iptables_io(ipaddr);
    
    
    return render_to_response('stats.html',{'ip':ipaddr,'io':io,'conn':conn})
    