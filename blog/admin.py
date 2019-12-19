from django.contrib import admin
from .models import Post,Comment
from tinymce.widgets import TinyMCE
from django.db import models


#admin.site.register(Post)

class Post_Admin(admin.ModelAdmin):
    fieldsets = [
        ("Name/Date&Time", {"fields": ["title","author","date_posted"]}),
        ("content", {"fields": ["content"]})
    ]
    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()}
    # }

admin.site.register(Post,Post_Admin)
admin.site.register(Comment)
