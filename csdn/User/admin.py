from django.contrib import admin

from User.models import *

admin.site.register(CMDBUser)
admin.site.register(User_group)
admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(User_permission)
admin.site.register(Permission_group)