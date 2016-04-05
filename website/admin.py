from django.contrib import admin
from models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language')

    class Meta:
        model = Article
