from django.db import models
from datetime import datetime
from goods.models import Goods
""" 用来去setting找AUTH_USER_MODEL"""
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,
                              verbose_name="商品")
    nums = models.IntegerField("购买数量", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        """ 用户唯一不重复 """
        unique_together = ["user", "goods"]

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)

""" 订单信息 """
class OrderInfo(models.Model):
    ORDER_STATUS = {
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("PAYING", "待支付"),
    }
    PAY_TYPE = {
        ("alipay", "支付宝"),
        ("wechat", "微信支付"),
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="用户")
    order_sn = models.CharField("订单编号", max_length=30, null=True, blank=True, unique=True)
    trade_no = models.CharField("交易号", max_length=100, null=True,blank=True,unique=True)
    pay_status = models.CharField("订单状态", choices=ORDER_STATUS, default="paying",max_length=30)
    pay_type = models.CharField("支付类型", choices=PAY_TYPE, default="alipay", max_length=30)
    post_script = models.CharField("订单留言", max_length=50)
    order_mount = models.FloatField("订单金额", default=0.0)
    pay_time = models.DateTimeField("支付时间", null=True, blank=True)
    """用户信息"""
    address = models.CharField("收货地址", max_length=100, default="")
    signer_name = models.CharField("签收人", max_length=20, default="")
    signer_mobile = models.CharField("签收人电话", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):

        return str(self.order_sn)

"""通过两个外键组成一张关联表"""

class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息",
                              related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name="商品")
    goods_num = models.IntegerField("商品数量", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
