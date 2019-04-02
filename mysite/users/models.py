from django.db import models

from django.db import models


class BlogUser(models.Model):
    """Account won't be necessarily for any more reason than
    giving comments on site"""
    username = models.CharField(max_length=40)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    site = models.URLField(null="True", blank=True)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='users/', default="users/default.jpg")

    def __str__(self):
        return self.username

    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/media/users/avatar.jpg'


class UserNewsletter(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    signed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class MessageNewsletter(models.Model):
    '''This will allow user to send email message to all
    newsletter participants in just one click then add mechanism
    to do it'''
    users = models.ManyToManyField(UserNewsletter)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    def send_all(self):
        '''This function will send email to all participiants'''
        pass

    def __str__(self):
        return f"{self.subject[:20]}... {self.send_date}"

# W przyszłości jeszcze będzie możliwość logowania się za pomocą githuba
# dlatego dodać potem jakiś mechanizm obsługiwania tych użytkowników
# szczególnie jeśli chodzi o dodawanie komentarzy oraz edycja profilu etc...
