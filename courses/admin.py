from django.contrib import admin
from .models import Course, FilesAdmin, Course1, Comment
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Course)
admin.site.register(Course1)
admin.site.register(FilesAdmin)
admin.site.register(Comment, MPTTModelAdmin)