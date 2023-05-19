from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.user.models import CustomUser
from django.contrib import auth


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'middle_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'staff_type', 'user_permissions',
                                       'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'middle_name', 'last_name', 'password1', 'password2',
                'is_active', 'is_staff', 'staff_type')}
         ),
    )
    list_display = ('username', 'first_name', 'middle_name', 'last_name', 'is_staff', 'staff_type')
    search_fields = ('first_name', 'last_name')
    ordering = ('date_joined',)

admin.site.unregister(auth.models.Group)