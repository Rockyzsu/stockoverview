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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',monitor_views.index),

    path('monitor',monitor_views.monitor),

    # 交割单
    path('jgd',delivery_views.delivery_order_view),

    path('query_post_json/',delivery_views.query_post_json),
    path('jz/',delivery_views.jingzhi),

]
