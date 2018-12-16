"""article serializers."""
from rest_framework import serializers

from article.models import Article


class AllArticlesSerializers(serializers.ModelSerializer):
    """所有文章序列化"""

    class Meta:
        models = Article
        fields = '__all__'


