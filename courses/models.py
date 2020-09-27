from django.db import models
from tinymce import HTMLField
from django_project.utils import unique_slug_generator
from django.conf import settings
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse



STATUS = ((0, "Draft"), (1, "Publish"))
# Create your models here.


class Course(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100, unique=True)
    adminupload = models.FileField(upload_to='media', blank=True)
    slug = models.SlugField(max_length=250, blank=True, unique_for_date='publish')
    thumbnail = models.ImageField()
    overview = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    content = HTMLField('content')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()

    def __str__(self):
        return self.title

    

def slug_generator(sender, instance, *args, **kwargs):
    """ Generate unique slug """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Course)

class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    class Meta:
        ordering = ['tree_id', 'lft']

    def __str__(self):
        return self.name


    


class Course1(models.Model):
    title = models.CharField(max_length=100)
    adminupload = models.FileField(upload_to='media', blank=True)
    thumbnail = models.ImageField()
    overview = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    content = HTMLField('content')

    def __str__(self):
        return self.title



class FilesAdmin(models.Model):
    upload = models.FileField(upload_to='media', null=None, blank=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
