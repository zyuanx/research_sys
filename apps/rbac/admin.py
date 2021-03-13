from django.contrib import admin

from apps.rbac.models import Permission, Role, UserInfo

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserInfo)
