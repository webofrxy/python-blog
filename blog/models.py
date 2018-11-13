from django.db import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name='用户名称', max_length=30,default='')
    description = models.TextField(verbose_name='用户介绍', max_length=200,default='')
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateField(verbose_name='修改时间', default=now)

    # 使对象在后台显示更友好
    def __str__(self):
        return self

    class Meta:
        ordering = ['name']
        verbose_name = '用户名称' #指定后台显示模型的名称
        verbose_name_plural = '用户列表' #指定后台显示模型的复数名称
        db_table = 'user' #数据库表名

class Tag(models.Model):
    name = models.CharField(verbose_name='标签名',max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间',default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间',default=now)

    def __str__(self):
        return self
    
    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'
        verbose_name_plural = '标签列表'
        db_table = 'tag'

class Category(models.Model):
    name = models.CharField(verbose_name='类别名称',max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间',default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间',default=now)

    def __str__(self):
        return self

    class Meta:
        ordering = ['name']
        verbose_name = '类别名称'
        verbose_name_plural = '分类列表'
        db_table = 'category'

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    pub_time = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'  # 指定后台显示模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型复数名称
        db_table = 'article'  # 数据库表名
        get_latest_by = 'created_time'
    
    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])
    # 下一篇
    def next_article(self):
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()
    # 上一篇
    def prev_article(self):
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()