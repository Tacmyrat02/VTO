from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('username', 'email', 'height', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'avatar')}),
        ('Body Measurements', {
            'fields': ('height', 'shoulder_width', 'waist'),
            'classes': ('collapse',)
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, CustomUserAdmin)