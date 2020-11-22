from django.db import transaction
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.visit.models import VisitLocation, VisitList
from apps.visit.serializers import VisitLocationSerializer, VisitListSerializer


class VisitLocationViewSet(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = VisitLocationSerializer
    queryset = VisitLocation.objects.all()

    ret = {'code': 200, 'msg': '数据获取成功', 'data': {}}

    def list(self, request, *args, **kwargs):
        response = super(VisitLocationViewSet, self).list(request, *args, **kwargs)
        self.ret['data'] = response.data
        return JsonResponse(self.ret)


class VisitListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = VisitListSerializer
    queryset = VisitList.objects.all()

    def list(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '数据获取成功'}
        user = request.query_params.get('user')
        visit_list = VisitList.objects.filter(user=user).first()
        if visit_list:
            serializer = VisitListSerializer(visit_list)
            ret['data'] = serializer.data
        return JsonResponse(ret)

    def create(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': '数据获取成功'}
        user = request.data.get('user')
        visit_list = VisitList.objects.filter(user=user).first()
        if visit_list:
            ret['code'] = 200
            # serializer = VisitListSerializer(visit_list)
            # self.ret['data'] = serializer.data
        else:
            location = request.data.get('location')
            with transaction.atomic():
                location_obj = VisitLocation.objects.select_for_update().filter(title=location).first()
                if location_obj.remain:
                    location_obj.remain = location_obj.remain - 1
                    location_obj.save()
                    response = super(VisitListViewSet, self).create(request, *args, **kwargs)
                    ret['code'] = 201
                    ret['msg'] = '申请成功'
                    ret['data'] = response.data
                else:
                    ret['code'] = 200
                    ret['msg'] = '余量不足，请重新选择'

        return JsonResponse(ret)
