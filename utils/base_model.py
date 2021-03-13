from datetime import datetime

from django.db import models
from mongoengine import *


class MongoBaseModel(Document):
    created_time = DateTimeField(verbose_name='创建时间')
    modified_time = DateTimeField(default=datetime.now, verbose_name='修改时间')

    def save(self, *args, **kwargs):
        if not self.created_time:
            self.created_time = datetime.now()
        self.modified_time = datetime.now()
        return super(MongoBaseModel, self).save(*args, **kwargs)

    meta = {'abstract': True}


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间', help_text='修改时间')
    is_deleted = models.BooleanField(default=False, verbose_name='删除标记', help_text='删除标记')

    class Meta:
        abstract = True
