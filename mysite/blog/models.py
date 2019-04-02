from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import BlogUser
from django.db.models.signals import pre_save
# from blog.utils import unique_slug_generator
from django.utils.text import slugify
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.tag_name

    def save(self):
        self.slug = slugify(self.tag_name)
        super().save()


class Article(models.Model):
    '''mechanism of giving likes/dislikes will be that after clicking like or dislike, there will be checked if current user 
    IP has already clicked one of these options he won't be able to rate once again and also 
    that will '''
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    thumbnail = ProcessedImageField(
        upload_to="img/thumbnails/",
        processors=[ResizeToFill(800, 400)],
        format='JPEG',
        options={'quality': 60},
        null=True,
        blank=True
    )
    content = RichTextUploadingField()
    categories = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    views = models.SmallIntegerField(blank=True, default=0)
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        published = "Published" if self.published_date else " Not Published"
        return f"{self.title[:30]}... {self.created_date} - {published}"

    def get_absolute_url(self):
        return reverse("article", kwargs={'pk': self.pk})

    def image_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return '/media/img/thumbnails/sample.jpg'

    def save(self, force_insert=False, force_update=False, using=None):
        self.slug = slugify(self.title)
        super().save()
        return reverse("home")
