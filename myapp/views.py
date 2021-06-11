from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
"""
HttpResponse函数是用来返回一个字符串的，后续返回的json格式字符串也是用它;
HttpResponseRedirect 是用来重定向到其他url上的;
render是用来返回html页面和页面初始数据的。
"""
# Create your views here.


@login_required
def welcome(request):
    print('welcome')
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})


def case_list(request):
    print('case_list')
    return render(request, 'case_list.html')


@login_required
def home(request):
    print('home')
    return render(request, 'home.html', {'username': 'wangshihua'})


def child(request, eid, oid):
    return render(request, eid)


def login(request):
    return render(request, 'login.html')


def login_action(request):
    username = request.GET['username']
    password = request.GET['password']

    # 联通django用户数据库，验证用户是否正确
    user = auth.authenticate(username=username, password=password)

    if user:
        # 进行正确的动作
        # return HttpResponseRedirect('/home/')
        auth.login(request, user)
        request.session['user'] = username
        return HttpResponse('success')
    else:
        # 告诉前端用户名或者密码不正确
        return HttpResponse('fail')


def register_action(request):
    username = request.GET['username']
    password = request.GET['password']

    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse('注册成功！')
    except:
        return HttpResponse('注册失败，用户名已经存在，请重新注册！')





