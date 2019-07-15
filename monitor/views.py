import datetime
import json
import re
import time

import redis
import tushare as ts
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
import easyquotation
from stockoverview import config
import pymysql

redis_server = redis.StrictRedis(config.redis,decode_responses=True,db=10)
codelist={}
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
    start=time.time()
    args = request.GET.get('code')
    # 区分代码还是名称
    if re.search('\d{6}',args):
        code=args
    else:
        code = str(redis_server.hget('codelist',args))
    q = easyquotation.use('qq')
    stockinfo = q.stocks(code)
    stockinfox = stockinfo[list(stockinfo.keys())[0]]
    stockinfox['datetime']=stockinfox['datetime'].strftime('%H:%M:%S')
    stockinfox['zdf']=stockinfox['涨跌(%)']
    print('call time use {} ms'.format((time.time()-start)*1000))
    return render_to_response('hangqing_sub.html', {'stockinfo': stockinfox})

# ajax
def hangqing_ajax(request):
    args = request.GET.get('code')
    print('接收到数据')
    # 区分代码还是名称
    if re.search('\d{6}',args):
        code=args
    else:
        code = str(redis_server.hget('codelist',args))
    q = easyquotation.use('qq')
    stockinfo = q.stocks(code)
    stockinfox = stockinfo[list(stockinfo.keys())[0]]
    stockinfox['datetime']=stockinfox['datetime'].strftime('%H:%M:%S')
    stockinfox['zdf']=stockinfox['涨跌(%)']
    return JsonResponse(stockinfox)


def update_stock(request):
    # 股票
    try:
        df = ts.get_stock_basics()
    except Exception as e:
        return JsonResponse({'status':0})

    else:
        for index,row in df.iterrows():
            redis_server.hset('codelist',row['name'],index)

    # 可转债
    try:
        db = pymysql.connect(config.mysql_host, config.mysql_user, config.mysql_password, config.mysql_db)
        cursor = db.cursor()
        cursor.execute('select 可转债代码,可转债名称 from tb_bond_jisilu')
        kzz_ret = cursor.fetchall()

    except Exception as e:
        return JsonResponse({'status':0})

    else:
        for item in kzz_ret:
            redis_server.hset('codelist',item[1],item[0])

        return JsonResponse({'status':1})


def hangqing_index(request):

    return render(request, 'realtime.html')
