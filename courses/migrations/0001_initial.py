# Generated by Django 3.1.1 on 2020-09-26 09:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('adminupload', models.FileField(blank=True, upload_to='media')),
                ('slug', models.SlugField(blank=True, max_length=250, unique_for_date='publish')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('overview', models.CharField(max_length=100)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('adminupload', models.FileField(blank=True, upload_to='media')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('overview', models.CharField(max_length=100)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(blank=True, null=None, upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.course')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='courses.comment')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
    ]
