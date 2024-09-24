from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, News, Comment




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'views', 'updated_at', 'is_published', 'author', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'slug', 'views', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'category')

    def get_image(self, obj):
        if obj.image:  # Agar rasm mavjud bo'lsa
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return mark_safe('<span>Rasm mavjud emas</span>')

    get_image.short_description = 'Rasm'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'user', 'content', 'created_at')
    list_display_links = ('id', 'news')


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)

