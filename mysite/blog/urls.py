from django.urls import path, include
from blog import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # article CRUD Views
    path('about/', views.AboutMeView.as_view(), name="about"),
    path("article/new/", views.ArticleCreateView.as_view(), name="article_create"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article"),
    path("article/edit/<int:pk>/",
         views.ArticleUpdateView.as_view(), name="article_edit"),
    path("article/publish/<int:pk>/",
         views.article_publish, name="article_publish"),
    path("article/unpublish/<int:pk>/",
         views.article_unpublish, name="article_unpublish"),
    path("article/delete/<int:pk>/",
         views.ArticleDeleteView.as_view(), name="article_delete"),
    # Draft list
    path("article/drafts/", views.DraftListView.as_view(), name="drafts"),
    # random article
    path("article/random/", views.random_article, name="random_article"),
    # about page




]
