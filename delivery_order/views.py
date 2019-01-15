import json

from django.shortcuts import render
from delivery_order.models import NameForms
from django.http import HttpResponse,JsonResponse
from delivery_order.models import TbDeliveryGjDjango

# Create your views here.
# 交割单查询页面

def delivery_order_view(request):

    if request.method=='GET':
        return render(request,'delivery.html')
    else:
        return HttpResponse('非法请求')


def query_post_json(request):

    name = request.GET.get('name')
    # 根据名称模糊查询

    objs = TbDeliveryGjDjango.objects.all().filter(证券名称__contains=name).order_by('-成交日期')
    result = []

    for obj in objs:
        d=obj.成交日期
        d_format = d.strftime('%Y-%m-%d')
        result.append([d_format,obj.证券名称,obj.成交均价,obj.成交金额,obj.成交数量,obj.操作])
    if not result:
        result = []
    return JsonResponse(result,safe=False)

def jingzhi(request):
    request.POST.get('')