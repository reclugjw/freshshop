from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models


class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
    )
    name = models.CharField('类别名', default="", max_length=30, help_text="类别名")
    code = models.CharField('类别code', default="", max_length=30, help_text="类别code")
    desc = models.TextField("类别描述", default="", help_text="类别描述")

    #目录树
    category_type = models.IntegerField("级别", choices=CATEGORY_TYPE, help_text="级别")
    """ 外码  """
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                                        blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat")
    is_tab = models.BooleanField("是否导航", default=False, help_text="是否导航")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


""" 商品设计 """


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    goods_sn = models.CharField("商品货号", max_length=100, default="")
    name = models.CharField("商品名", max_length=100)
    click_num = models.IntegerField("点击数", default=0)
    sold_num = models.IntegerField("商品销售量", default=0)
    fav_num = models.IntegerField("收藏数", default=0)
    goods_num = models.IntegerField("库存量", default=0)
    market_price = models.FloatField("市场价格", default=0)
    shop_price = models.FloatField("本店价格", default=0)
    goods_brief = models.TextField("商品简短描述", default=0)
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              toolbars="full",filePath="goods/files/",
                              upload_settings={"imageMaxSize": 1204000},
                              settings={}, default='')
    ship_free = models.BooleanField("是否包邮", default=True)
    """ 商品封面图 """
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField("是否是新品", default=False)
    is_hot = models.BooleanField("是否是热销品", default=False)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsImage(models.Model):
    """ 商品轮播图？"""
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品",
                              related_name="image")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '商品轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

""" 首页轮播的图，是大图"""
class Banner(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField("轮播顺序", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

""" 广告 """
class HotSearchWords(models.Model):
    keywords = models.CharField("热搜词", default="", max_length=20)
    index = models.IntegerField("排序", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '热搜排行'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


# Create your models here.
