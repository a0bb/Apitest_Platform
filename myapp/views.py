from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from myapp.models import DBTucao
"""
HttpResponse函数是用来返回一个字符串的，后续返回的json格式字符串也是用它;
HttpResponseRedirect 是用来重定向到其他url上的;
render是用来返回html页面和页面初始数据的。
"""
# Create your views here.


@login_required
def welcome(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


def case_list(request):
    print('case_list')
    return render(request, 'case_list.html')


@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


def child(request, eid, oid):
    # 它只做一件事，就是真实的返回
    # 我们目标html, 在这里就是home.html，其中的eid，就是获取url中的(?P < eid >.+) 的值，也就是我们welcome.html中的
    # {{whichHTML}} ，也就是我们后台函数返回的子页面html的真实名字。
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
        # 给浏览器写入session信息，没有session则进入不了登陆后的页面
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


# 退出登陆
def logout(request):
    auth.logout(request)
    """
    这里我们是可以直接用HttpResponseRedirect重定向函数 给直接重定到登陆页面/login/的。
    因我前面讲了，如果是a标签的href 或者form表单提交 这种会触发页面刷新的情况，后端函数都可以直接让用户重定向。
    但是如果是异步请求$.get() 则不可以。
    """
    return HttpResponseRedirect('/login/')


# 吐槽函数
def pei(request):
    tucao_text = request.GET['tucao_text']
    DBTucao.objects.create(user=request.user.username, text=tucao_text)
    # 这里之所以返回空字符串，是因为我们前端页面写死了，无论返回什么都弹窗说吐槽成功！
    return HttpResponse('')


# 帮助文档
def api_help(request):
    return render(request, 'welcome.html', {'whichHTML': 'help.html', 'oid': ''})
