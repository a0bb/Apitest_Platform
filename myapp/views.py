from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
"""
HttpResponse函数是用来返回一个字符串的，后续返回的json格式字符串也是用它;
HttpResponseRedirect 是用来重定向到其他url上的;
render是用来返回html页面和页面初始数据的。
"""
# Create your views here.


def welcome(request):
    print('welcome')
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})


def case_list(request):
    print('case_list')
    return render(request, 'case_list.html')


def home(request):
    print('home')
    return render(request, 'home.html', {'username': 'wangshihua'})


def child(request, eid, oid):
    return render(request, eid)


def login(request):
    return render(request, 'login.html')
