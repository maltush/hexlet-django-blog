# hexlet_django_blog/article/views.py
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def index(request: HttpRequest, tags: str, article_id: int) -> HttpResponse:
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

def home_redirect(request: HttpRequest):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
