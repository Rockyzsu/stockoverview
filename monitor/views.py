import datetime
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import easyquotation


# Create your views here.

def index(request):
    # 显示主页
    return render(request, 'index.html')


# 监控持仓股
def monitor(request):
    title = '实时监测'
    result = ['H', 'I', 'J', 'K']
    context = {}
    context['title'] = title
    context['aaa'] = result
    return render(request, 'monitor.html', context)


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 行情
def hangqing(request):
    code = request.GET.get('code')

    q = easyquotation.use('qq')
    stockinfo = q.stocks(code)
    stockinfox = stockinfo[list(stockinfo.keys())[0]]
    stockinfox['datetime']=stockinfox['datetime'].strftime('%H:%M:%S')
    stockinfox['zdf']=stockinfox['涨跌(%)']
    return render_to_response('hangqing_sub.html', {'stockinfo': stockinfox})


def hangqing_index(request):
    return HttpResponse('待开发')
