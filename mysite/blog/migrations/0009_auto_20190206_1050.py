# Generated by Django 2.1.4 on 2019-02-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecomment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='articlecommentresponse',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='articlecommentresponse',
            name='response_comment',
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
        migrations.DeleteModel(
            name='ArticleCommentResponse',
        ),
    ]