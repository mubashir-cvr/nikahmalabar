from django.contrib import admin

from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
 # Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Importand dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )




    
    
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Image)

@admin.register(models.UserEducationLocationContact)
class UserEducationLocationContactAdmin(admin.ModelAdmin):
    list_display = ('highestEducation','user')

@admin.register(models.UserProperties)
class UserPropertiesAdmin(admin.ModelAdmin):
    list_display = ('name','user')
