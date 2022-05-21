from django.contrib import admin
from .models import Movie, MyComment,Comment,Instagram
from django.utils.translation import gettext_lazy as _

from django_comments_xtd.admin import XtdCommentsAdmin


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'status', 'year_of_production', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content',]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.register(Instagram)
