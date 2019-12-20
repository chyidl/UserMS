from django.db import models

# Create your models here.
class User(models.Model):
    """
    用户表
    """
    gender = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='未知')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        verbose_name = 'User'
        verbose_name_plural = 'User'