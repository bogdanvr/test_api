from django.contrib import admin

from pages.models import Ads


@admin.register(Ads)
class UserAdmin(admin.ModelAdmin):
    list_display = ('page_id', 'title', 'views')
    # readonly_fields = ('created', 'user')
    # list_filter = ('user',)
