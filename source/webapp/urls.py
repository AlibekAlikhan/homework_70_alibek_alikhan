from django.urls import path

from webapp.views.articles import ArticleView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeletedView, ArticleDeleteConfirmView


urlpatterns =[
    path('', ArticleView.as_view(), name="index_article"),
    path('article', ArticleView.as_view(), name="index_article"),
    path('article/create', ArticleCreateView.as_view(), name="create_article"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="detail_view"),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name="article_update"),
    path('article/<int:pk>/delit', ArticleDeletedView.as_view(), name="article_delit"),
    path('article/<int:pk>/delit/confirm', ArticleDeleteConfirmView.as_view(), name="confirm")
]