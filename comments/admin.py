from django.contrib import admin
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'post', 'user']
    list_filter = ['created_at']
    search_fields = ['content']


