# Generated by Django 2.1.4 on 2019-01-22 09:27

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='img/thumbnails/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.IntegerField(choices=[(1, 'Python'), (2, 'Data science'), (3, 'Machine Learning')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('dislikes', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=True)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('dislikes', models.SmallIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.BlogUser')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCommentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.ArticleComment')),
                ('response_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_comment', to='blog.ArticleComment')),
            ],
        ),
    ]