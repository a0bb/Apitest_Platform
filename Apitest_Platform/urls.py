"""Apitest_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^welcome/$', welcome),  # 进入主页
    url(r'^case_list/$', case_list),  # 进入用例列表页
    url(r'^home/$', home),  # 进入首页
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),  # 返回子页面
    url(r'^login/$', login),  # 学生登录页面
    url(r'^login_action/$', login_action),  # 登陆跳转
    url(r'^register_action/$', register_action),  # 注册
    url(r'^accounts/login/$', login),  # 非登录状态自动跳回登录页面
    url(r'^logout/$', logout),  # 退出
    url(r'^pei/$', pei),  # 匿名吐槽
    url(r'^help/$', api_help),  # 帮助文档
    url(r'^project_list/$', project_list),  # 进入项目列表
    url(r'^delete_project/$', delete_project),  # 删除项目
    url(r'^add_project/$', add_project),  # 添加项目
    url(r'^apis/(?P<id>.*)/$', open_apis),  # 进入接口库
    url(r'^cases/(?P<id>.*)/$', open_cases),  # 进入用例设置

    url(r'^project_set/(?P<id>.*)/$', open_project_set),  # 进入项目设置
    url(r'^save_project_set/(?P<id>.*)/$', save_project_set),  # 保存项目设置

    url(r'^project_api_add/(?P<Pid>.*)/$', project_api_add),  # 新增api
    url(r'^project_api_del/(?P<id>.*)/$', project_api_del),  # 删除api
    url(r'^save_bz/$', save_bz),  # 保存备注
    url(r'^get_bz/$', get_bz),  # 获取备注

    url(r'^api_save/$', api_save),  # 保存接口
    url(r'^get_api_data/$', get_api_data),  # 获取接口数据
    url(r'^api_send/$', api_send),  # 发送接口数据

]
