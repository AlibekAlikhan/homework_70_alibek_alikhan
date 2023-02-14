from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.views.db import Cat

c = Cat()


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, "article_create.html")
    print(request.POST)


def state_cat(make):
    match make:
        case "play":
            c.play()
        case "feed":
            c.eat()
        case "sleep":
            c.slepp()


def cat_stats(request: WSGIRequest):
    make = request.POST.get('make')
    name = request.GET.get('name')
    state_cat(make)
    return render(request, 'article.html', context={
        'name': name,
        'year': c.year,
        'happiness': c.happiness,
        'satiety': c.satiety,
        'make': make,
        'sleep': c.sleep,
        'img': c.img
    })
