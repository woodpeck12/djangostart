from django.contrib import admin

# Register your models here.

#woodpeck -- add
from .models import Post

admin.site.register(Post)