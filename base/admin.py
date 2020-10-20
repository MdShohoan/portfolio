from django.contrib import admin

# Register your models here.

from .models import Post, Tag,Contact

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Tag)
