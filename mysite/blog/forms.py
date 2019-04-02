from django import forms
from blog.models import Article


class ArticleForm1(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("title", "thumbnail", "categories")
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }


class ArticleForm2(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("content", )
