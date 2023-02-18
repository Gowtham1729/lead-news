from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'url')


# Register your models here.
admin.site.register(News, NewsAdmin)
