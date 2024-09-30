from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    pass
