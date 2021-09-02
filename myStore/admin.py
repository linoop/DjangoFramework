from django.contrib import admin
from . models import Game, Book


class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Game, GamesAdmin)
admin.site.register(Book)
