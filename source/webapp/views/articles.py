from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Article


def article_view(request: WSGIRequest):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "tasks.html", context=context)
