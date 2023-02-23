from django.urls import path

from webapp.views.articles import article_view, article_create, detail_view, article_update


urlpatterns =[
    path('', article_view, name="index_article"),
    path('article', article_view, name="index_article"),
    path('article/create', article_create, name="create_article"),
    path('article/<int:pk>', detail_view, name="detail_view"),
    path('article/<int:pk>/update', article_update, name="article_update")
]