from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FinalProject.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'gender', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'first_name', 'last_name',
                'gender'),
        }),
    )
