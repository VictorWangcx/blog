"""article.apis."""

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from article.serializers import AllArticlesSerializers
from article.models import Article


class AllArticles(ListAPIView):
    """展示所有的博文"""

    view_name = "all_articles"
    serializer_class = AllArticlesSerializers

    def get_queryset(self):
        queryset = Article.objects.filter(is_delete=False).order_by("-create_time")
        return queryset








