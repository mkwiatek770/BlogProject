from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
# models
from blog.models import Article, Tag
from users.models import BlogUser
# cbv
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
# queryset or
from django.db.models import Q
# forms
from blog.forms import ArticleForm1, ArticleForm2
# register new template filter
from django.template.defaulttags import register
# django message framework
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# timezone
from django.utils import timezone
# handling permissions
from django.contrib.auth.mixins import PermissionRequiredMixin
from random import randint

#################TODO############################
# 1.Poprawić wygląd nawigacji tych 2 ikonek do zmiany tła(musza być dalej od siebie)
# 9. zapoznać się z https: // www.youtube.com/watch?v = cXYVE28igkE i być może zastosować
# 17. Odpowiednio zmodyfikować widoki, tak, żeby jako admin widizeć więcej
# 23. Obsługa błędów
# 26. rozważyć czy w belce aside - top articles umieścić ogólny ranking, czy będzie on obliczany w zależności od kategorii etc...
# 29. pomyśleć o zapisywaniu sesji/ciasteczek z preferencjami kolorystycznymi dla danego użytkownika


#################################################


# home page
class HomeView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/home1.html"
    paginate_by = 5
    search = None
    # tymczasowo paginacja na 2 ale potem będzie 10/20

    def get_queryset(self):

        qs = super().get_queryset()
        qs = qs.filter(published_date__isnull=False)
        # categories filtering
        if self.request.GET.get("category"):
            qs = qs.filter(categories__slug=self.request.GET['category'])\
                .order_by("-published_date")
            self.search = Tag.objects.get(
                slug=self.request.GET['category']).tag_name
        else:
            qs = qs.order_by('-published_date')

        # search filtering
        if self.request.GET.get("search"):
            search_phrase = self.request.GET['search']
            qs = qs.filter(Q(title__icontains=search_phrase) |
                           Q(content__icontains=search_phrase))
            self.search = self.request.GET['search']

        return qs

    def get_context_data(self, **kwargs):
        # top articles
        context = super().get_context_data(**kwargs)
        articles = self.get_queryset()
        context['popular_articles'] = articles.order_by('-views')[:5]
        # tags
        tags = Tag.objects.all()
        t_counts = {}
        for t in tags:
            t_counts[t] = Article.objects.filter(categories=t).count()
        # reversed sorted dictionary of tags
        context['t_counts'] = sorted(
            t_counts.items(), key=lambda kv: kv[1])[::-1][:5]

        context['search'] = self.search

        return context

    # filter to have access to dictionary syntax key.value in django templates
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)


class ArticleDetailView(DetailView):

    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"

    def get(self, request, slug):
        article = self.get_object()
        if not article.published_date:
            return redirect(reverse("home"))

        article.views += 1
        article.save()

        return render(request, self.template_name, {
            self.context_object_name: article
        })

    # def handle_no_permission(self):
    # return redirect(reverse("home"))


# CRUD Views - Article

class ArticleCreateView(PermissionRequiredMixin, CreateView):

    form_class = ArticleForm1
    second_form_class = ArticleForm2
    template_name = "blog/article_form.html"

    permission_required = "request.user.is_staff"

    def handle_no_permission(self):
        return redirect(reverse("home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form1' not in context:
            context['form1'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):

        form1 = self.get_form_class()
        form1 = self.get_form(form1)
        form2 = self.second_form_class
        form2 = self.get_form(form2)

        # validate
        if form1.is_valid() and form2.is_valid():

            title = form1.cleaned_data['title']
            thumbnail = form1.cleaned_data['thumbnail']
            categories = form1.cleaned_data['categories']
            content = form2.cleaned_data['content']

            article = Article.objects.create(
                title=title,
                thumbnail=thumbnail,
                content=content,
            )
            article.categories.set(categories)

            messages.add_message(request, messages.SUCCESS,
                                 "Article created succesfully now it's in drafts")
            return redirect(reverse("drafts"))
        else:
            messages.add_message(request, messages.WARNING,
                                 "Something went wrong")
            return self.get(request)


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm1
    second_form_class = ArticleForm2
    template_name = "blog/article_form.html"
    context_object_name = "article"
    permission_required = "request.user.is_staff"

    def handle_no_permission(self):
        return redirect(reverse("home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form1' not in context:
            context['form1'] = self.form_class(instance=self.get_object())
        if 'form2' not in context:
            context['form2'] = self.second_form_class(
                instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):

        form1 = ArticleForm1(request.POST, request.FILES)
        form2 = ArticleForm2(request.POST,)

        if form1.is_valid() and form2.is_valid():
            title = form1.cleaned_data['title']
            thumbnail = form1.cleaned_data['thumbnail']
            categories = form1.cleaned_data['categories']
            content = form2.cleaned_data['content']

            article = self.get_object()
            article.title = title
            if thumbnail:
                article.thumbnail = thumbnail
            article.categories.set(categories)
            article.content = content
            article.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Article Updated Successfully")
            return redirect(reverse("drafts"))
        else:
            messages.add_message(request, messages.WARNING,
                                 "Something went wrong")
            return self.get(request)


class ArticleDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "blog/article_confirm_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"
    permission_required = "request.user.is_staff"
    success_message = "Article was removed succesfully"

    def handle_no_permission(self):
        return redirect(reverse("home"))

    def get_success_message(self, cleaned_data):
        return self.success_message


def article_publish(request, pk):
    if not request.user.is_staff:
        return redirect(reverse("home"))
    article = Article.objects.get(pk=pk)
    article.published_date = timezone.now()
    article.save()

    messages.success(request, "Article was published")

    return redirect(reverse('article_edit', kwargs={'pk': pk}))


def article_unpublish(request, pk):
    if not request.user.is_staff:
        return redirect(reverse("home"))
    article = Article.objects.get(pk=pk)
    article.published_date = None
    article.save()

    messages.warning(request, "Article was unpublished")
    return redirect(reverse("article_edit", kwargs={"pk": pk}))


# Draft Views

class DraftListView(PermissionRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/drafts.html"
    paginate_by = 10
    permission_required = "request.user.is_staff"

    def handle_no_permission(self):
        return redirect(reverse("home"))

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(published_date__isnull=True).order_by('-modified_date')


# About me view
class AboutMeView(TemplateView):
    template_name = 'blog/about.html'

    # random article


def random_article(request):
    articles = Article.objects.filter(published_date__isnull=False)
    nr = randint(0, len(articles) - 1)
    article = articles[nr]

    return redirect(f"/{article.slug}")
