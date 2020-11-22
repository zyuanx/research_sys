from django.db import models

from utils.base_model import BaseModel


class VisitList(BaseModel):
    user = models.CharField(max_length=32, verbose_name='学号')
    name = models.CharField(max_length=32, verbose_name='姓名')
    tel = models.CharField(max_length=11, verbose_name='电话')
    college = models.CharField(max_length=32, verbose_name='学院')
    stuclass = models.CharField(max_length=64, verbose_name='班级')
    location = models.CharField(max_length=32, verbose_name='地点')

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['created_time']


class VisitLocation(BaseModel):
    title = models.CharField(max_length=32, verbose_name='名称')
    remain = models.SmallIntegerField(verbose_name='余量')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_time']
