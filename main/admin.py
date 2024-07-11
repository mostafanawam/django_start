from django.contrib import admin

from main.form import CustomUserCreationForm
from main.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        'email','password',
        # 'is_staff','is_superuser','is_enabled'
    ]
    list_display = (
        'id',
        "username",
        'email',
        'is_staff',
        'is_enabled',
        'is_superuser',
        'last_login',
    ) 
    list_filter = ('is_staff',)
admin.site.register(User, UserAdmin)



