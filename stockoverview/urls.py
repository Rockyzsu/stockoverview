"""stockoverview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monitor import views as monitor_views
from delivery_order import views as delivery_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',monitor_views.index),

    path('monitor',monitor_views.monitor),

    # 交割单
    path('jgd',delivery_views.delivery_order_view),

    path('query_post_json/',delivery_views.query_post_json),
    path('post_win/',delivery_views.query_win),

    path('jz/',delivery_views.jingzhi_view),

    # 更新净值
    path('update_jz/',delivery_views.jingzhi),
    path('blacklist/',delivery_views.blacklist),
    path('query_blacklist/',delivery_views.query_blacklist),
    path('get_jz/',delivery_views.get_jz),

    #行情
    path('hq/',monitor_views.hangqing),
    path('hq_index/',monitor_views.hangqing_index),

]

urlpatterns += staticfiles_urlpatterns()