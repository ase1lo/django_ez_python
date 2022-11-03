
from django.contrib import admin
from .models import Topic, Author, Category, Genre, Country
from django import forms
from .forms import AuthorForm
from django.utils.safestring import mark_safe



class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'nickname', 'birthday', 'genre', 'country')
    list_display = ('name', 'nickname', 'birthday', 'genre', 'country')


class TopicAdmin(admin.ModelAdmin): 
    list_display = ('title', 'get_photo', 'is_published', 'create_time', 'update_time')
    fields = ('title', 'content', 'author', 'category', 'is_published', 'photo')
    readonly_fields = ('create_time', 'update_time')

    list_filter = ('title', 'is_published', 'create_time', 'update_time')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{ obj.photo.url }" width="150">')
 
    get_photo.short_description = 'Фото'



admin.site.register(Topic, TopicAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Author, AuthorAdmin)
