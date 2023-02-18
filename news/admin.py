from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "source_name", "author")


# Register your models here.
admin.site.register(News, NewsAdmin)
