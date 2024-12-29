from django.contrib import admin
from .models import Posts,Author,Tags

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter= ("author","tags","date",)
    list_display=("title","author","date",)

admin.site.register(Posts,PostsAdmin)
admin.site.register(Author)
admin.site.register(Tags)