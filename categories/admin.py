from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','published','created_at')
    list_filter = ('published','created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    ordering = ('title',)
