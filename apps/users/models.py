from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_model import BaseModel
from utils.custom_storage import ImageStorage


class UserInfo(AbstractUser, BaseModel):
    nickname = models.CharField(max_length=16, verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', default='avatar/default.jpg', blank=True,
                               storage=ImageStorage(), verbose_name='头像')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['created_time']
