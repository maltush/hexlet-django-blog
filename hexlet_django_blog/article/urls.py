from django.urls import path

from hexlet_django_blog.article import views


urlpatterns = [
path("", views.index, name="article_index"),
path("str:tags [blocked]/int:article\_id [blocked]/", views.index, name="article"),
]

