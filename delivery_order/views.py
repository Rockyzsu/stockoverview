import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from delivery_order.models import TbDeliveryGjDjango, TbJingzhi2019, TbJingzhi2020, TbBlacklist, TbDeliveryHbDjango, \
    TbJingzhiHB2020, TbJingzhiHB2021

from django.views.decorators.csrf import csrf_exempt
from stockoverview.config import init_money_hb, init_money_gj, hs300_start_index
from delivery_order.get_index import get_index

# Create your views here.
# 交割单查询页面

def delivery_order_view(request):
    if request.method == 'GET':
        return render(request, 'delivery.html')
    else:
        return HttpResponse('非法请求')


def delivery_order_hb_view(request):
    if request.method == 'GET':
        return render(request, 'delivery_hb.html')
    else:
        return HttpResponse('非法请求')


def query_post_json(request):
    name = request.GET.get('name')
    if name is None:
        return JsonResponse([], safe=False)

    # 根据名称模糊查询
    name = name.strip()

    objs = TbDeliveryGjDjango.objects.all().filter(证券名称__contains=name).order_by('-成交日期')
    result = []

    for obj in objs:
        d = obj.成交日期
        d_format = d.strftime('%Y-%m-%d %H:%M:%S')
        result.append([d_format, obj.证券名称, obj.证券代码, round(obj.成交均价, 2), obj.成交金额, obj.成交数量, obj.操作])
    if not result:
        result = []
    return JsonResponse(result, safe=False)


def query_post_json_hb(request):
    name = request.GET.get('name')
    if name is None:
        return JsonResponse([], safe=False)

    # 根据名称模糊查询
    name = name.strip()

    objs = TbDeliveryHbDjango.objects.all().filter(证券名称__contains=name).order_by('-成交日期')
    result = []

    for obj in objs:
        d = obj.成交日期
        d_format = d.strftime('%Y-%m-%d %H:%M:%S')
        result.append([d_format, obj.证券名称, obj.证券代码, round(obj.成交价格, 2), obj.成交金额, obj.成交数量, obj.委托类别])
    if not result:
        result = []
    return JsonResponse(result, safe=False)


def query_win(request):
    name = request.GET.get('name')
    # 根据名称模糊查询

    objs = TbDeliveryGjDjango.objects.all().filter(证券名称__contains=name).order_by('-成交日期')
    result = []
    sum = 0
    for obj in objs:
        d = obj.成交日期
        d_format = d.strftime('%Y-%m-%d %H:%M:%S')
        result.append([d_format, obj.证券名称, obj.证券代码, obj.成交均价, obj.成交金额, obj.成交数量, obj.操作])
        p = obj.成交均价 * obj.成交数量
        sum += p

    if not result:
        result = []
    sum = round(sum * -1, 2)
    result.append(['总盈亏', '*', '*', '*', '*', '*', sum])
    return JsonResponse(result, safe=False)


def jingzhi_view_gj(request, year):
    return render(request, 'jingzhi.html', {'year': year})


def jingzhi_view_hb(request, year):
    print(year)
    return render(request, 'jingzhi_hb.html', {'year': year})


@csrf_exempt
def jingzhi(request):
    '''
    2020年之前的
    :param request:
    :return:
    '''
    money = request.POST.get('money')
    year = request.POST.get('year')

    # import tushare as ts

    if year == '2019':

        start_value = hs300_start_index.get(year, 0)
        current = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')

        df = get_index()
        current_v = df[df['code'] == '000300']['close'].values[0]
        hs_latest = round(current_v / start_value, 4)

        obj = TbJingzhi2019.objects.all().order_by('-date')
        last_day_assert = obj[0].assert_field
        try:
            money = float(money)
        except Exception as e:
            resp = {'status': 0}
            return JsonResponse(resp, safe=False)

        profit = (money - last_day_assert) / last_day_assert * 100
        profit = round(profit, 2)
        netvalue = round(money / 60000, 4)
        obj, ret = TbJingzhi2019.objects.get_or_create(date=current, assert_field=money, profit=profit,
                                                       netvalue=netvalue, hs300=hs_latest)
        raise_value = round((netvalue - 1) * 100, 2)

    elif year == '2020':

        start_value = hs300_start_index.get(year, 0)

        current = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
        df = get_index()

        current_v = df[df['code'] == '000300']['close'].values[0]
        hs_latest = round(current_v / start_value, 4)

        obj = TbJingzhi2020.objects.all().order_by('-date')
        last_day_assert = obj[0].assert_field

        try:
            money = float(money)
        except Exception as e:
            resp = {'status': 0}
            return JsonResponse(resp, safe=False)

        profit = (money - last_day_assert) / last_day_assert * 100
        profit = round(profit, 2)
        netvalue = round(money / 150000, 4)
        obj, ret = TbJingzhi2020.objects.get_or_create(date=current, assert_field=money, profit=profit,
                                                       netvalue=netvalue, hs300=hs_latest)
        raise_value = round((netvalue - 1) * 100, 2)

    if ret:
        resp = {'status': 1, 'netvalue': netvalue, 'raise_value': raise_value, 'hs_latest': hs_latest}
    else:
        resp = {'status': 0}

    return JsonResponse(resp, safe=False)


def year_variable(year):
    '''
    根据不同年份初始化
    :param year:
    :return:
    '''

    if year == '2020':
        start_value = hs300_start_index.get(year, 0)

        obj = TbJingzhiHB2020
        init_money = init_money_gj

    elif year == '2021':
        start_value = hs300_start_index.get(year, 0)

        obj = TbJingzhiHB2021
        init_money = init_money_hb  # 初始资金

    elif year == '2022':
        start_value = hs300_start_index.get(year, 0)

        obj = TbJingzhiHB2021
        init_money = init_money_hb  # 初始资金
    else:
        start_value = 0
        init_money = 0
        obj = None

    return start_value, init_money, obj


@csrf_exempt
def jingzhi_hb(request):
    '''
    更新华宝的净值
    :param request:
    :return:
    '''
    money = request.POST.get('money')
    year = request.POST.get('year')
    cash = request.POST.get('cash')
    money = float(money)
    cash = float(cash)
    position = round((money - cash) / money * 100, 0)

    # import tushare as ts

    start_value, init_money, jz_model = year_variable(year)
    current = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = get_index()

    current_v = df[df['code'] == '000300']['close'].values[0]
    hs_latest = round(current_v / start_value, 4)

    obj = jz_model.objects.all().order_by('-date')

    last_day_assert = obj[0].assert_field

    try:
        money = float(money)
    except Exception as e:
        resp = {'status': 0}
        return JsonResponse(resp, safe=False)

    profit = (money - last_day_assert) / last_day_assert * 100
    profit = round(profit, 2)
    netvalue = round(money / init_money, 4)

    obj, ret = jz_model.objects.get_or_create(date=current, assert_field=money, profit=profit,
                                              netvalue=netvalue, hs300=hs_latest, cash=cash, position=position)
    raise_value = round((netvalue - 1) * 100, 2)

    if ret:
        resp = {'status': 1, 'netvalue': netvalue, 'raise_value': raise_value, 'hs_latest': hs_latest,
                'postion': position}
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


def get_jz(request, year):
    # current = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    if year == '2019':
        objs = TbJingzhi2019.objects.all().order_by('-date')
    elif year == '2020':
        objs = TbJingzhi2020.objects.all().order_by('-date')
    else:
        print('obj not exists')
    ret = []
    for obj in objs:
        ret.append([obj.date.strftime('%Y-%m-%d'), obj.assert_field, obj.netvalue, obj.profit, obj.hs300])

    if ret:
        resp = ret
    else:
        resp = None
    # print(resp)

    return JsonResponse(resp, safe=False)


def get_jz_hb(request, year):
    # 获取净值
    # current = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    ret = []

    if year == '2020':
        objs = TbJingzhiHB2020.objects.all().order_by('-date')
        for obj in objs:
            ret.append([obj.date.strftime('%Y-%m-%d'), obj.assert_field, obj.netvalue, obj.profit, obj.hs300, 0,
                        0])
    else:
        try:
            year_int = int(year)
        except Exception as e:
            print(e)
        else:
            objs = TbJingzhiHB2021.objects.filter(date__year=year_int).all().order_by('-date')
            for obj in objs:
                ret.append(
                    [obj.date.strftime('%Y-%m-%d'), obj.assert_field, obj.netvalue, obj.profit, obj.hs300, obj.cash,
                     obj.position])

    if ret:
        resp = ret
    else:
        resp = None

    return JsonResponse(resp, safe=False)
