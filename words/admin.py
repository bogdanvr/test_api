from django.contrib import admin

from words.models import Words, Phrases


@admin.register(Words)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translate')
    search_fields = ('word',)

@admin.register(Phrases)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'phrase', 'translate')
    search_fields = ('word',)
