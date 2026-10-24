from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'city', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Profile & Address', {
            'fields': (
                'phone_number',
                'profile_image',
                'address_line_1',
                'address_line_2',
                'city',
                'state',
                'postal_code',
                'country'
            )
        }),
    )
