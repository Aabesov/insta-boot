from django.contrib import admin

from post.models import HashTag, Image, Post

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(HashTag)
