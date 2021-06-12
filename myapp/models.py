from django.db import models


class DBTucao(models.Model):
    user = models.CharField(max_length=30, null=True)  # 吐槽人的用户名
    text = models.CharField(max_length=1000, null=True)  # 吐槽信息
    ctime = models.DateTimeField(auto_now=True)  # 吐槽信息创建时间

    def __str__(self):
        return self.text + str(self.ctime)