from django.contrib.auth import authenticate

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserInfo
from apps.users.serializers import UserReadSerializer, UserRegisterSerializer, UserAuthSerializer, UserLogoutSerializer
from utils.custom_response.base_response import BaseResponse


class UserRegisterViewSet(mixins.CreateModelMixin,
                          GenericViewSet):
    """
    用户注册、添加视图
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = UserRegisterSerializer
    queryset = UserInfo.objects.all()

    def create(self, request, *args, **kwargs):
        response = super(UserRegisterViewSet, self).create(request, *args, **kwargs)
        return BaseResponse(message="创建成功", data=response.data)


class UserAuthViewSet(mixins.CreateModelMixin,
                      GenericViewSet):
    """
    用户认证视图
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = UserAuthSerializer
    queryset = UserInfo.objects.all()

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
            return BaseResponse(message="认证成功", data=token_data)
        else:
            return BaseResponse(code=20001, message="用户名或密码错误")


class UserReadViewSet(mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    用户信息获取视图
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserReadSerializer
    queryset = UserInfo.objects.all().order_by('created_time')

    def list(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return BaseResponse(message='信息获取成功', data=serializer.data)


class UserLogoutViewSet(mixins.CreateModelMixin,
                        GenericViewSet):
    """
    退出
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserLogoutSerializer
    queryset = UserInfo.objects.all().order_by('created_time')

    def create(self, request, *args, **kwargs):
        instance = request.user
        RefreshToken.for_user(instance)
        return BaseResponse(message='退出成功')