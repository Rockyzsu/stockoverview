import datetime
import json

from django.shortcuts import render
from delivery_order.models import NameForms
from django.http import HttpResponse, JsonResponse
from delivery_order.models import TbDeliveryGjDjango, TbJingzhi, TbBlacklist

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# Create your views here.
# 交割单查询页面

def delivery_order_view(request):
    if request.method == 'GET':
        return render(request, 'delivery.html')
    else:
        return HttpResponse('非法请求')


def query_post_json(request):
    name = request.GET.get('name')
    # 根据名称模糊查询

    objs = TbDeliveryGjDjango.objects.all().filter(证券名称__contains=name).order_by('-成交日期')
    result = []

    for obj in objs:
        d = obj.成交日期
        d_format = d.strftime('%Y-%m-%d %H:%M:%S')
        result.append([d_format, obj.证券名称, obj.成交均价, obj.成交金额, obj.成交数量, obj.操作])
    if not result:
        result = []
    return JsonResponse(result, safe=False)


def jingzhi_view(request):
    return render(request, 'jingzhi.html')


@csrf_exempt
def jingzhi(request):
    money = request.POST.get('money')
    current = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    obj = TbJingzhi.objects.all().order_by('-date')
    last_day_assert = obj[0].assert_field
    try:
        money = float(money)
    except Exception as e:
        resp = {'status': 0}
        return JsonResponse(resp, safe=False)

    profit = (money - last_day_assert) / last_day_assert * 100
    profit = round(profit, 2)
    netvalue = round(money / 60000, 4)
    obj, ret = TbJingzhi.objects.get_or_create(date=current, assert_field=money, profit=profit, netvalue=netvalue)
    raise_value = round((netvalue-1),2)*100
    if ret:
        resp = {'status': 1,'netvalue':netvalue,'raise_value':raise_value}
    else:
        resp = {'status': 0}
    return JsonResponse(resp, safe=False)


def blacklist(request):
    title = 'A股黑名单列表'
    context = {'title': title}

    return render(request, 'blacklist.html', context=context)


def query_blacklist(request):
    objs = TbBlacklist.objects.all()
    result = []

    for obj in objs:
        d = obj.date
        d_format = d.strftime('%Y-%m-%d')
        result.append([d_format, obj.code, obj.name, obj.reason])
    if not result:
        result = []
    return JsonResponse(result, safe=False)
