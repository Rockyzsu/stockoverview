from django.shortcuts import render
from delivery_order.models import NameForms
from django.http import HttpResponse,JsonResponse
from delivery_order.models import TbDeliveryGjDjango

# Create your views here.
# 交割单查询页面

def delivery_order_view(request):

    if request.method=='GET':
        print('GET')
        form = NameForms()
        return render(request,'delivery.html',{'form':form})
    else:
        print('POST')
        form=NameForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            objs = TbDeliveryGjDjango.objects.filter(证券名称=name)
            # print(obj)
            for obj in objs:
                print(obj.本次金额,obj.成交数量)
            return HttpResponse('get')


def query(request):
    name = request.GET.get('name')
    objs = TbDeliveryGjDjango.objects.filter(证券名称=name)
    # print(obj)
    result = []
    for obj in objs:
        # print(obj.本次金额, obj.成交数量)
        result.append(str(obj.本次金额)+' '+str(obj.成交数量)+'<br>')
    # print('name',name)
    # result = {'ret':name + ' append'}
    # return JsonResponse(result)
    if not result:
        result = '无查询结果<br>'
    return HttpResponse(''.join(result))
