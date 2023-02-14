from django.urls import path

from webapp.views.articles import article_view, article_create

urlpatterns =[
    path('', article_view),
    path('article/create', article_create)
]