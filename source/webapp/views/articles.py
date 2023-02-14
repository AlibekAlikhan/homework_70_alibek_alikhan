from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

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
        "create_at": request.POST.get('create_at')
    }
    Article.objects.create(**article_data)
    return redirect(f"/")
