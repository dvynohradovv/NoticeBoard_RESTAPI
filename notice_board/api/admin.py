from django.contrib import admin
from .models import Post, UserDetail, PostLike

# Register your models here.
admin.site.register(Post)
admin.site.register(UserDetail)
admin.site.register(PostLike)
