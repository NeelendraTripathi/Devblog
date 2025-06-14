# blog/admin.py
from django.contrib import admin
from .models import post

# The @admin.register(Post) decorator does the same thing as
# admin.site.register(Post, PostAdmin). It's just cleaner.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    # We will add our configuration options here.
    list_display = ('pk', 'title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    # Allow searching by title and content.
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}
    # The 'pass' keyword means "do nothing". It's a placeholder.