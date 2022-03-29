from django.db import models


class Category(models.Model):
    """ 博客分类模型 """
    name = models.CharField(max_length=32, verbose_name='分类名称')
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='分类描述')
    add_date = models.DateField(auto_now=True, verbose_name="添加日期")
    mod_date = models.DateField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ 文章标签模型 """
    name = models.CharField(max_length=10, verbose_name='文章标签')
    add_date = models.DateField(auto_now=True, verbose_name="添加日期")
    mod_date = models.DateField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """ 文章模型 """
    title = models.CharField(max_length=60, verbose_name="文章标题")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='文章描述')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    content = models.TextField(verbose_name="文章详情")
    tags = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name='文章标签')
    add_date = models.DateField(auto_now=True, verbose_name="添加日期")
    mod_date = models.DateField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title