from rest_framework.viewsets import ModelViewSet

from utils.custom_response.base_response import BaseResponse


class BaseViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return BaseResponse(data=serializer.data, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(data=serializer.data)

    def update(self, request, *args, **kwargs):
        """
        put /entity/{pk}/
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return BaseResponse(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        delete /entity/{pk}/
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return BaseResponse(message='数据删除成功.')
