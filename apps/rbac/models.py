from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_model import BaseModel
from utils.storage import ImageStorage


class Permission(BaseModel):
    """
    权限表
    """
    MENU_ITEMS = (
        (0, '目录'),
        (1, '菜单'),
        (2, '接口')
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='标题')
    method = models.CharField(max_length=50, verbose_name='方法')
    menu = models.IntegerField(choices=MENU_ITEMS, default=0, verbose_name='类型')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='父权限')

    def __str__(self):
        return self.title


class Role(BaseModel):
    """
    角色表
    """
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField(verbose_name='拥有的权限', to='Permission', blank=True)
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="描述")

    def __str__(self):
        return self.title


class UserInfo(AbstractUser, BaseModel):
    """
    用户表
    """
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    roles = models.ManyToManyField(verbose_name='拥有的角色', to='Role', blank=True)
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="上级主管")
    avatar = models.ImageField(storage=ImageStorage, upload_to='avatar/%Y/%m/%d', default='avatar/default.jpg',
                               blank=True,
                               verbose_name='头像')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['create_time']
