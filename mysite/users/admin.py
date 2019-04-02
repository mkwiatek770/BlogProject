from django.contrib import admin
from users.models import BlogUser, UserNewsletter, MessageNewsletter
# Register your models here.

@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
	pass


@admin.register(UserNewsletter)
class UserNewsletterAdmin(admin.ModelAdmin):
	pass


@admin.register(MessageNewsletter)
class MessageNewsletterAdmin(admin.ModelAdmin):
	pass


