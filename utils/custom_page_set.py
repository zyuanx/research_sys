from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class PageSet(pagination.PageNumberPagination):
    # 每页显示多少个
    page_size = 10
    # 默认每页显示3个
    page_size_query_param = "size"
    # 最大页数
    max_page_size = 100
    # 获取页码数的
    page_query_param = "page"

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))
