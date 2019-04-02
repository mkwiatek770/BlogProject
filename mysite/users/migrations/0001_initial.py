# Generated by Django 2.1.4 on 2019-01-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('site', models.URLField(blank=True, null='True')),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.ImageField(default='users/default.jpg', upload_to='users/')),
            ],
        ),
        migrations.CreateModel(
            name='MessageNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('send_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('signed_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='messagenewsletter',
            name='users',
            field=models.ManyToManyField(to='users.UserNewsletter'),
        ),
    ]