from django.contrib import admin

from myapp.models import *


# 建表之后，注册到admin后台
admin.site.register(DBTucao)
admin.site.register(DBHomeHref)
admin.site.register(DBProject)
admin.site.register(DBApis)
