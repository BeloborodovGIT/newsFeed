from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'photo', 'get_photo', 'created_at')
    readonly_fields = ('get_photo', 'created_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75px>')

    get_photo.short_description = 'Миниатюра'


admin.site.register(News, NewsAdmin)
