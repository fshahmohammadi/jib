from django.contrib import admin
from groups.models import Group
from groups.models import GroupTrans
from groups.models import GroupBalance

admin.site.register(Group)
admin.site.register(GroupTrans)
admin.site.register(GroupBalance)