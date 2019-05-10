from django.contrib import admin
from .models import Image, category, location

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Image, ArticleAdmin)
admin.site.register(category)
admin.site.register(location)