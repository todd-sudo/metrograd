from django.contrib import admin

from .models import Tenant, Task


admin.site.register(Tenant)
admin.site.register(Task)
