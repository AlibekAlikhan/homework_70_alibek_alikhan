from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article


def article_view(request: WSGIRequest):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "tasks.html", context=context)


def article_create(request: WSGIRequest):
    if request.method == "GET":
        return render(request, "article_create.html")
    print(request.POST)
    article_data = {
        "status": request.POST.get('status'),
        "text": request.POST.get('text'),
        "detail_text": request.POST.get('text'),
        "create_at": request.POST.get('create_at')
    }
    article = Article.objects.create(**article_data)
    return redirect("detail_view", pk=article.pk)


def detail_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "detail_article.html", context={
        'article': article
    })
