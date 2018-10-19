# coding=utf-8
"""mycms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'cms.views.index'),
    url(r'^notfound/$', 'cms.views.notfound'),# 404页面
    url(r'^favorite/$', 'cms.views.favorite'),
    url(r'^blog/$', 'cms.views.blog'), # 博客页
    url(r'^edit_article/(?P<id>[0-9]+)/$', 'cms.views.edit_article'),
    url(r'^create_blog/$', 'cms.views.create_blog'), # 创建博客页面
    url(r'^blog_detail/$', 'cms.views.blog_detail'), #博客列表页面
    url(r'^sub_article/$', 'cms.views.sub_article'),
    url(r'^count_blog/$', 'cms.views.count_blog'), #博客柱状图
    url(r'^tag_manage/$','cms.views.tag_manage'), # 标签管理

]
