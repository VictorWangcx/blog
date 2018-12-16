"""article.models"""
from uuid import uuid4

from django.db import models

from mdeditor.fields import MDTextField

from common.common import PathAndRename


class Article(models.Model):
    """博客文章"""
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField('题目', max_length=50)
    desc = models.CharField('简述', max_length=100)
    photo = models.ImageField(
        verbose_name='商品图片',
        upload_to=PathAndRename('article/%Y/%m')
    )
    content = MDTextField(verbose_name='博客正文', default='')  # 注意为MDTextField()
    category = models.ForeignKey('ArticleCategory',
                                 verbose_name="分类",
                                 related_name='article_category', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User',
                             verbose_name="标签",
                             related_name="article_user",on_delete=models.CASCADE)

    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'article'
        verbose_name = verbose_name_plural = '博客'


class ArticleTag(models.Model):
    """标签"""
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    tag_name = models.CharField('标签名称', max_length=30)
    article = models.ForeignKey('Article',
                                verbose_name="文章",
                                related_name="article_tag",
                                null=True, on_delete=models.CASCADE)


class ArticleCategory(models.Model):
    """博客种类"""
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    type = models.CharField('标签名称', max_length=30)






