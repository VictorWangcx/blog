"""article.url."""
from django.urls import path

from article.apis import AllArticles

urlpatterns = [
    path('articles/', AllArticles.as_view()),
]