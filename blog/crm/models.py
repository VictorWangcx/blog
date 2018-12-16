"""crm.models"""
import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils.crypto import salted_hmac


class CrmUser(models.Model):
    """后台用户表 用户表"""
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    account = models.CharField('账号', max_length=32, unique=True)
    name = models.CharField('姓名', max_length=32)

    password = models.CharField('密码', max_length=80)

    permissions = models.CharField('权限', max_length=1024)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    mobile = models.CharField('手机号', max_length=11, default='', blank=True)

    is_active = models.BooleanField('是否可用', default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=['password'])

        return check_password(raw_password, self.password, setter)

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(key_salt, self.password).hexdigest()

    class Meta:
        verbose_name = 'CRM用户'
        verbose_name_plural = 'CRM用户'

    def __str__(self):
        return self.account

