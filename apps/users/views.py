from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserInfo
from apps.users.serializers import UserReadSerializer, UserRegisterSerializer, UserAuthSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    用户注册、添加视图
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = UserRegisterSerializer
    queryset = UserInfo.objects.all()

    ret = {'code': 201, 'msg': '创建用户成功', 'data': {}}

    def create(self, request, *args, **kwargs):
        response = super(UserRegisterViewSet, self).create(request, *args, **kwargs)
        self.ret['data'] = response.data
        return JsonResponse(self.ret)


class UserAuthViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    用户认证视图
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = UserAuthSerializer
    queryset = UserInfo.objects.all()
    ret = {'code': 200, 'msg': '认证信息获取成功', 'data': {}}

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            token_data = {
                'token': str(refresh.access_token),
                'refresh': str(refresh),
            }
            self.ret['data'] = token_data
            return JsonResponse(self.ret)
        else:
            return JsonResponse({'code': 400, 'msg': '用户名或密码错误'})


class UserReadViewSet(mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    用户信息获取视图
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserReadSerializer
    queryset = UserInfo.objects.all().order_by('created_time')
    ret = {'code': 200, 'msg': '用户信息获取成功', 'data': {}}

    def list(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        self.ret['data'] = serializer.data
        return JsonResponse(self.ret)
