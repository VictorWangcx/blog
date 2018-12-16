from django.db import models

from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    """用户表"""
    uuid = models.UUIDField(unique=True)
    account = models.CharField('账号', max_length=32, unique=True)
    mobile = models.CharField('手机号', max_length=20, blank=True)
    photo = models.ImageField('头像照片', upload_to='media/user/photo/')
    remark = models.CharField('备注', max_length=100, blank=True)
    permissions = models.CharField('权限', max_length=1024)

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户'


