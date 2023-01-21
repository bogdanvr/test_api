from django.contrib import admin

from chat.models import Message


@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    list_display = ('created', 'user')
    readonly_fields = ('created', 'user')
    list_filter = ('user',)
