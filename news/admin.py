from django.contrib import admin

# Register your models here.

from .models import News, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_slug')
    prepopulated_fields = {'cat_slug': ('cat_name',)}
    fieldsets = [
        ('Main Details', {'fields': ['cat_name','cat_slug']}),
    ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'category')
    list_filter = ['created_on']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    fieldsets = (
        ('Main Info', {
            'fields': ['title', 'slug', 'author', 'status', 'category'],
            'classes': ('baton-tabs-init', 'baton-tab-fs-content', 'baton-tab-fs-image', ),

        }),
        ('Content', {
            'fields': ('content', ),
            'classes': ('tab-fs-content', ),

        }),
        ('Image', {
            'fields': ('cover', ),
            'classes': ('tab-fs-image', ),
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
