from mongoengine import *

from utils.base_model import MongoBaseModel


class ResearchList(MongoBaseModel):
    STATUS_ITEMS = (
        (0, '停止收集'),
        (1, '正常收集')
    )
    title = StringField(max_length=20, required=True, verbose_name='标题')
    desc = StringField(max_length=200, required=True, verbose_name='描述')
    fieldsValue = DictField(required=True, verbose_name='字段值')
    detail = ListField(required=True, verbose_name='调研表')
    rules = DictField(required=True, verbose_name='验证字段值')
    confirm = StringField(max_length=10, default='提交', verbose_name='提交按钮文字')
    status = IntField(default=1, choices=STATUS_ITEMS, verbose_name='状态')

    @queryset_manager
    def objects(self, query_set):
        return query_set.order_by('created_time', )

    meta = {'collection': 'research_list'}


class ResearchData(MongoBaseModel):
    research_id = StringField(required=True, verbose_name='调研id')
    user = DictField(required=True, verbose_name='用户信息')
    detail = DictField(required=True, verbose_name='调研数据')

    @queryset_manager
    def objects(self, query_set):
        return query_set.order_by('research_id', 'created_time')

    meta = {'collection': 'research_data'}
