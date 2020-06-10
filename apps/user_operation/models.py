from django.db import models
from datetime import  datetime
from goods.models import Goods
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class UserFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    province = models.CharField("省份", max_length=20, default="")
    city = models.CharField("城市", max_length=50, default="")
    district = models.CharField("区域", max_length=100, default="")
    address = models.CharField("详细地址", max_length=100, default="")
    signer_name = models.CharField("签收人", max_length=20, default="")
    signer_mobile = models.CharField("签收人电话", max_length=11, default="")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES ={
        (1, "留言"),
        (2, "投诉"),
        (3, "咨询"),
        (4, "售后"),
        (5, "求购")
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型：1（留言），2（投诉），3（咨询），4（售后），5（求购）")
    subject = models.CharField("主题", max_length=100, default="")
    message = models.TextField("内容", help_text="留言内容", default="" )
    file = models.FileField(upload_to="message/images/", verbose_name="所要上传的图片", help_text="所要上传的图片")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.subject
