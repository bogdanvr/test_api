from django.contrib import admin

from tax.models import Tax


@admin.register(Tax)
class UserAdmin(admin.ModelAdmin):
    list_display = ('created', 'price')
