import collections
import os

from django.conf import settings
from django.http import JsonResponse, FileResponse
from rest_framework import mixins
from rest_framework_mongoengine import viewsets
from rest_framework_mongoengine.viewsets import GenericViewSet

from apps.research.models import ResearchList, ResearchData
from apps.research.serializers import ResearchListSerializer, ResearchDataSerializer
from utils.custom_response.base_response import BaseResponse


class ResearchListViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchListSerializer
    queryset = ResearchList.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            return []
        return super(ResearchListViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).list(request, *args, **kwargs)
        return BaseResponse(message="调研信息获取成功", data=response.data)

    def create(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).create(request, *args, **kwargs)
        return BaseResponse(message="调研问卷创建成功", data=response.data)

    def retrieve(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).retrieve(request, *args, **kwargs)
        return BaseResponse(message="调研信息获取成功", data=response.data)

    def partial_update(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).partial_update(request, *args, **kwargs)
        return BaseResponse(message="调研更新成功", data=response.data)

    def destroy(self, request, *args, **kwargs):
        super(ResearchListViewSet, self).destroy(request, *args, **kwargs)
        return BaseResponse(message="调研删除成功")


class ResearchDataViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    permission_classes = []
    serializer_class = ResearchDataSerializer
    queryset = ResearchData.objects.all()

    # lookup_field = 'user__username'
    my_filter_fields = ('user__username', 'research_id')  # specify the fields on which you want to filter

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            if '__' in field:
                field_value = self.request.query_params.get(field.split('__')[1])
            else:
                field_value = self.request.query_params.get(field)
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = super().get_queryset()
        filtering_kwargs = self.get_kwargs_for_filtering()
        if filtering_kwargs:
            queryset = queryset.filter(**filtering_kwargs)
        return queryset

    # 获取数据
    def list(self, request, *args, **kwargs):
        response = super(ResearchDataViewSet, self).list(request, *args, **kwargs)
        return BaseResponse(message="数据获取成功", data=response.data)

    # 提交数据
    def create(self, request, *args, **kwargs):
        response = super(ResearchDataViewSet, self).create(request, *args, **kwargs)
        return BaseResponse(message="数据提交成功", data=response.data)


def export_xlsx(title, data, filename):
    """
    导出xlsx文件
    :param title: dict，表头
    :param data: dict，数据
    :param filename:
    :return:
    """
    import xlsxwriter
    filename = '%s.xlsx' % filename
    filepath = os.path.join(settings.MEDIA_ROOT, filename)

    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()
    if len(data):
        # 写标题

        dict_data = collections.OrderedDict()
        dict_data['id'] = data[0]['id']
        dict_data.update(data[0]['user'])
        dict_data.update(data[0]['detail'])
        dict_data['research_id'] = data[0]['research_id']
        dict_data['modified_time'] = data[0]['modified_time']
        dict_data['created_time'] = data[0]['created_time']

        j = 0
        for item in dict_data.keys():
            if item in title.keys():
                worksheet.write(0, j, title[item])
            else:
                worksheet.write(0, j, item)
            j += 1

        for i in range(len(data)):
            dict_data = collections.OrderedDict()
            dict_data['id'] = data[i]['id']
            dict_data.update(data[i]['user'])
            dict_data.update(data[i]['detail'])
            dict_data['research_id'] = data[i]['research_id']
            dict_data['modified_time'] = data[i]['modified_time']
            dict_data['created_time'] = data[i]['created_time']

            j = 0
            for item in dict_data.keys():
                worksheet.write(i + 1, j, dict_data[item])
                j += 1
    workbook.close()
    return FileResponse(open(filepath, 'rb'), filename=filename)


class ResearchExportViewSet(mixins.ListModelMixin,
                            GenericViewSet):
    permission_classes = []
    serializer_class = ResearchDataSerializer
    queryset = ResearchData.objects.all()

    def list(self, request, *args, **kwargs):
        research_id = self.request.query_params.get("research_id")
        # 获取调研数据
        research_data_obj = ResearchData.objects.filter(research_id=research_id).all()
        serializer = ResearchDataSerializer(research_data_obj, many=True)
        data = serializer.data

        # 获取调研字段标题
        research_obj = ResearchList.objects.with_id(research_id)
        research_data = ResearchListSerializer(research_obj, many=False)
        title_dict = collections.OrderedDict()
        for item in research_data.data['detail']:
            title_dict[item['fieldId']] = item['label']

        return export_xlsx(title_dict, data, research_id)
