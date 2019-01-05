from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Pass')


# 监控持仓股
def monitor(request):
    title = '实时监测'
    result = ['H', 'I', 'J', 'K']
    context = {}
    context['title'] = title
    context['aaa'] = result
    return render(request, 'monitor.html', context)
