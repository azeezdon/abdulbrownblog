from django.db import models
from tinymce import HTMLField
from django_project.utils import unique_slug_generator

from django.conf import settings
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()


    def __str__(self):
        return self.user.username



class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, blank=True, unique_for_date='publish')
    overview = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # comment_count =models.IntegerField(default=0)
    # view_count =models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    content = HTMLField('content')
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    #   comments = GenericRelation(Comment)

    def __str__(self):
        return self.title





def slug_generator(sender, instance, *args, **kwargs):
    """ Generate unique slug """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)



class Comment(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class MPTTMeta:
        order_insertion_by = ['publish']

    class Meta:
        ordering = ['tree_id', 'lft']

    def __str__(self):
        return self.name
