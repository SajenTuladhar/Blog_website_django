from django.contrib import admin
from .models import Posts,Author,Caption

# Register your models here.

admin.site.register(Posts)
admin.site.register(Author)
admin.site.register(Caption)