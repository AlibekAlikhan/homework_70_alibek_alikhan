from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article


def article_view(request: WSGIRequest):
    articles = Article.objects.exclude(is_deleted=True)
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
        "detail_text": request.POST.get('detail_text')
    }
    article = Article.objects.create(**article_data)
    return redirect("detail_view", pk=article.pk)


def article_update(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.status = request.POST.get('status')
        article.text = request.POST.get('text')
        article.detail_text = request.POST.get('detail_text')
        article.save()
        return redirect("detail_view", pk=article.pk)
    else:
        return render(request, "article_update.html", context={
            'article': article
        })


def detail_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "detail_article.html", context={
        'article': article
    })


def deleted(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "delete_confirm.html", context={
        'article': article
    })


def deleted_confirm(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("index_article")
