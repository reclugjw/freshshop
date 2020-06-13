
# Create your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """ 用户模型类 """
    GENDER_CHOICE = {
        ("male", u"男"),
        ("female", u"女")
    }
    """ 手机注册 注册表"""
    name = models.CharField("姓名", max_length=35, null=True, blank=True)
    gender = models.CharField("性别", max_length=100, choices=GENDER_CHOICE, default="female")
    birthday = models.DateField("出生年月", null=True, blank=True)
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)
    mobile = models.CharField("手机号", max_length=11)
    nation = models.CharField("民族", max_length=20, null=True, blank=True)

    """ 为模型类起中文名 """
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    """ 把一个类的实例转换成str """
    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    """ 验证码 """
    mobile = models.CharField("手机号", max_length=11)
    code = models.CharField("验证码", max_length=10)
    add_time = models.DateTimeField("添加时间", default=datetime.now())

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
