# Create your views here.
from django.http import HttpResponse
from DNF.stats.info import Statistics 
from DNF import conf
from django.shortcuts import render_to_response, redirect

stats = Statistics()


def user_stats(request):
    ipaddr = request.META['REMOTE_ADDR']
    conn = stats.get_conntrack(ipaddr)
    io = stats.get_iptables_io(ipaddr)
    limited = stats.is_limited(ipaddr)
    limit = [conf.bandwidth.max_connections_user,conf.bandwidth.rx_max_user,conf.bandwidth.tx_max_user]
    
    return render_to_response('stats.html',{'ip':ipaddr,'io':io,'conn':conn, 'limited': limited, 'limit':limit[0]})
    