from django.db import models


class Customer(models.Model):
    """
    客户表
    """
    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.CharField(verbose_name='年龄', max_length=32)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    company = models.CharField(verbose_name='公司', max_length=32)

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
    付费记录
    """
    customer = models.ForeignKey(verbose_name='关联客户', null=True, on_delete=models.SET_NULL, to='Customer')
    money = models.IntegerField(verbose_name='付费金额')
    create_time = models.DateTimeField(verbose_name='付费时间', auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.customer, self.money)
