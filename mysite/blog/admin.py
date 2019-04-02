from django.contrib import admin
from blog.models import Article, Tag
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
