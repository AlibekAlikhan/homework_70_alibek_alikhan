from django.urls import path

from webapp.views.articles import article_view

urlpatterns =[
    path('', article_view)
]