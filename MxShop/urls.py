"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include,re_path
from django.views.static import serve #上传文件处理函数
from .settings import MEDIA_ROOT  #从配置中导入
import xadmin
from django.db import models
from goods.views_base import GoodsListView
import DjangoUeditor
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import CategoryViewSet
#from goods.views import GoodsListView,
# from goods.views_base import GoodsListView
#from extra_apps import xadmin, DjangoUeditor
router = DefaultRouter()
router.register(r'categorys', CategoryViewSet, basename="categorys")
urlpatterns = [
        path('xadmin/', xadmin.site.urls),
        path('ueditor/', include('DjangoUeditor.urls')),
        re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
        #path('docs',include_docs_urls(title='freshshop')),
        path('api-auth/',include('rest_framework.urls')),

        path('goods/', GoodsListView.as_view(),name="goods-list"),
        re_path('^', include(router.urls)),
        #path('goods/', goods_list,name="goods-list"),

       # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
       # path('goods/', GoodsListView(), name='good-list')
]
