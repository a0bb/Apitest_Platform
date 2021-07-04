from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json

from myapp.models import DBTucao, DBHomeHref, DBProject, DBApis
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
    # 它只做一件事，就是真实的返回我们目标html, 在这里就是home.html
    # 其中的eid，就是获取url中的(?P < eid >.+) 的值，也就是我们welcome.html中的{{whichHTML}}
    # 也就是我们后台函数返回的子页面html的真实名字。
    print(eid)
    res = child_json(eid, oid)
    return render(request, eid, res)


# 控制不同的页面返回不同的数据：数据分发器
def child_json(eid, oid=''):
    res = {}
    if eid == 'home.html':
        data = DBHomeHref.objects.all()
        res = {'hrefs': data}
    if eid == 'project_list.html':
        data = DBProject.objects.all()
        print(data)
        res = {'projects': data}
    if eid == 'P_apis.html':
        project = DBProject.objects.filter(id=oid)[0]
        apis = DBApis.objects.filter(project_id=oid)
        res = {'project': project, 'apis': apis}
    if eid == 'P_cases.html':
        project = DBProject.objects.filter(id=oid)[0]
        res = {'project': project}
    if eid == 'P_project_set.html':
        project = DBProject.objects.filter(id=oid)[0]
        res = {'project': project}

    return res


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


# 项目列表
def project_list(request):
    return render(request, 'welcome.html', {'whichHTML': 'project_list.html', 'oid': ''})


# 删除项目
def delete_project(request):
    id_ = request.GET['id']
    DBProject.objects.filter(id=id_).delete()
    DBApis.objects.filter(project_id=id_).delete()
    return HttpResponse('')


# 添加项目
def add_project(request):
    project_name = request.GET['project_name']
    project_remark = request.GET['project_remark']
    DBProject.objects.create(
        name=project_name,
        remark=project_remark,
        user=request.user.username,
        other_user=''
    )
    return HttpResponse('')


# 进入接口库
def open_apis(request, id):
    project_id = id
    return render(
        request,
        'welcome.html',
        {'whichHTML': 'P_apis.html', 'oid': project_id}
    )


# 进入用例设置
def open_cases(request, id):
    project_id = id
    return render(
        request,
        'welcome.html',
        {'whichHTML': 'P_cases.html', 'oid': project_id}
    )


# 进入项目设置
def open_project_set(request, id):
    project_id = id
    return render(
        request,
        'welcome.html',
        {'whichHTML': 'P_project_set.html', 'oid': project_id}
    )


# 保存项目设置
def save_project_set(request, id):
    project_id = id
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DBProject.objects.filter(id=project_id).update(name=name, remark=remark, other_user=other_user)

    return HttpResponse('')


# 新增接口
def project_api_add(request, Pid):
    project_id = Pid
    DBApis.objects.create(project_id=project_id)
    return HttpResponseRedirect(f'/apis/{project_id}/')


# 删除接口
def project_api_del(request, id):
    project_id = DBApis.objects.get(id=id).project_id
    DBApis.objects.filter(id=id).delete()
    return HttpResponseRedirect(f'/apis/{project_id}/')


# 保存备注 des
def save_bz(request):
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DBApis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse('')


# 获取备注
def get_bz(request):
    api_id = request.GET['api_id']
    bz = DBApis.objects.get(id=api_id).des
    return HttpResponse(bz)


# 接口保存
def api_save(request):
    api_id = request.GET['api_id']
    api_name = request.GET['api_name']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']

    if ts_body_method == '返回体':
        api = DBApis.objects.get(id=api_id)
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body
        if ts_body_method in [None, '']:
            return HttpResponse('请先选择好请求体编码格式和请求体，再点击Send按钮发送请求！')
    else:
        ts_api_body = request.GET['ts_api_body']
        DBApis.objects.filter(id=api_id).update(
            last_body_method=ts_body_method, last_api_body=ts_api_body
        )

    DBApis.objects.filter(id=api_id).update(
        name=api_name,
        api_method=ts_method,
        api_url=ts_url,
        api_header=ts_header,
        api_host=ts_host,
        body_method=ts_body_method,
        api_body=ts_api_body
    )
    return HttpResponse('success')


# 获取接口数据
def get_api_data(request):
    api_id = request.GET['api_id']
    api = DBApis.objects.filter(id=api_id).values()[0]
    return HttpResponse(json.dumps(api), content_type='application/json')


# 发送接口数据
def api_send(request):
    api_id = request.GET['api_id']
    api_name = request.GET['api_name']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']

    if ts_body_method == '返回体':
        api = DBApis.objects.get(id=api_id)
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body
        if ts_body_method in [None, '']:
            return HttpResponse('请先选择好请求体编码格式和请求体，再点击Send按钮发送请求！')
    else:
        ts_api_body = request.GET['ts_api_body']
        DBApis.objects.filter(id=api_id).update(
            last_body_method=ts_body_method, last_api_body=ts_api_body
        )

    return HttpResponse('{"code": 200}')
