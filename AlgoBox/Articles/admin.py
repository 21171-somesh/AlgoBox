from django.contrib import admin

from .forms import CreateArticle
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = CreateArticle
    fields = ['title', 'slug', 'content', 'status']