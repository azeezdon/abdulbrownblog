from django.contrib import admin
from .models import Post,Author,PostView,Comment
from mptt.admin import MPTTModelAdmin
# Register your models here.

admin.site.register(Author)
admin.site.register(PostView)
admin.site.register(Post)
admin.site.register(Comment, MPTTModelAdmin)






