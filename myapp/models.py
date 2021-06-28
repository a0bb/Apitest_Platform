from django.db import models


class DBTucao(models.Model):
    user = models.CharField(max_length=30, null=True)  # 吐槽人的用户名
    text = models.CharField(max_length=1000, null=True)  # 吐槽信息
    ctime = models.DateTimeField(auto_now=True)  # 吐槽信息创建时间

    def __str__(self):
        return self.text + str(self.ctime)


class DBHomeHref(models.Model):
    name = models.CharField(max_length=30, null=True)  # 超链接名称
    href = models.CharField(max_length=1000, null=True)  # 超链接内容

    def __str__(self):
        return self.name


class DBProject(models.Model):
    name = models.CharField(max_length=100, null=True)  # 项目名
    remark = models.CharField(max_length=1000, null=True)  # 项目备注
    user = models.CharField(max_length=15, null=True)  # 项目创建者姓名
    other_user = models.CharField(max_length=200, null=True)  # 项目其他成员

    def __str__(self):
        return self.name


class DBApis(models.Model):
    project_id = models.CharField(max_length=10, null=True)  # 项目id
    name = models.CharField(max_length=100, null=True)  # 接口名称
    api_method = models.CharField(max_length=10, null=True)  # 请求方式
    api_url = models.CharField(max_length=1000, null=True)  # url
    api_header = models.CharField(max_length=1000, null=True)  # 请求头
    api_login = models.CharField(max_length=10, null=True)  # 是否带登录态
    api_host = models.CharField(max_length=100, null=True)  # 域名
    des = models.CharField(max_length=100, null=True)  # 描述
    body_method = models.CharField(max_length=20, null=True)  # 请求体编码格式
    api_body = models.CharField(max_length=1000, null=True)  # 请求体
    result = models.TextField(null=True)  # 返回体 因为长度巨大，所以用大文本方式存储
    sign = models.CharField(max_length=10, null=True)  # 是否验签
    file_key = models.CharField(max_length=50, null=True)  # 文件key
    file_name = models.CharField(max_length=50, null=True)  # 文件名
    public_header = models.CharField(max_length=1000, null=True)  # 全局变量-请求头

    def __str__(self):
        return self.name
