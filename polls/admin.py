from django.contrib import admin
from common.models.country import *
from common.models.money import *
from common.models.users import *

# adminアカウントを作成する
# python manage.py createsuperuser
# root:rootpass and icloud account
# Questionモデルを作成する
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(MoneyType)
admin.site.register(Money)
admin.site.register(AdminUser)