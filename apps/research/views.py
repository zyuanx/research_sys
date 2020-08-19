from django.http import JsonResponse
from rest_framework import mixins
from rest_framework_mongoengine.viewsets import GenericViewSet

from apps.research.models import ResearchList, ResearchData
from apps.research.serializers import ResearchListSerializer, ResearchDataSerializer


class ResearchListViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    serializer_class = ResearchListSerializer
    queryset = ResearchList.objects.all()
    ret = {'code': 200, 'msg': '', 'data': {}}

    def list(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).list(request, *args, **kwargs)
        self.ret['code'] = 200
        self.ret['msg'] = '调研信息获取成功'
        self.ret['data'] = response.data
        return JsonResponse(self.ret)

    def create(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).create(request, *args, **kwargs)
        self.ret['code'] = 201
        self.ret['msg'] = '调研问卷创建成功'
        self.ret['data'] = response.data
        return JsonResponse(self.ret)

    def retrieve(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).retrieve(request, *args, **kwargs)
        self.ret['data'] = response.data
        return JsonResponse(self.ret)

    def partial_update(self, request, *args, **kwargs):
        response = super(ResearchListViewSet, self).partial_update(request, *args, **kwargs)
        self.ret['code'] = 201
        self.ret['msg'] = '调研更新成功'
        self.ret['data'] = response.data
        return JsonResponse(self.ret)


class ResearchDataViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    serializer_class = ResearchDataSerializer
    queryset = ResearchData.objects.all()
    ret = {'data': {}, 'msg': "success", 'code': 200, }

    def list(self, request, *args, **kwargs):
        response = super(ResearchDataViewSet, self).list(request, *args, **kwargs)
        self.ret['code'] = 200
        self.ret['msg'] = '数据获取成功'
        self.ret['data'] = response.data
        return JsonResponse(self.ret)

    def create(self, request, *args, **kwargs):
        response = super(ResearchDataViewSet, self).create(request, *args, **kwargs)
        self.ret['code'] = 201
        self.ret['msg'] = '提交成功'
        self.ret['data'] = response.data
        return JsonResponse(self.ret)
