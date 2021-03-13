from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.rbac.models import UserInfo, Permission, Role
from apps.rbac.serializers import PermissionSerializer, RoleSerializer, UserAuthLoginSerializer, \
    UserAuthInfoSerializer, UserAuthLogoutSerializer, ChangePasswordSerializer, UserInfoSerializer, UserBlankSerializer, \
    PasswordSerializer


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = None


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = None


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()

    permission_prefix = 'userinfo'

    def get_serializer_class(self):
        serializer_class = UserInfoSerializer
        if self.action == 'reset_password':
            serializer_class = UserBlankSerializer
        return serializer_class

    @action(detail=True, methods=['post'])
    def reset_password(self, request, pk=None):
        instance = self.get_object()
        instance.set_password('123456')
        instance.save()
        return Response('密码已重置为123456')

    @action(detail=True, methods=['put'])
    def update_avatar(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthViewSet(GenericViewSet):
    queryset = UserInfo.objects.all()

    def get_permissions(self):
        if self.action == 'login':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = None
        if self.action == 'login':
            serializer_class = UserAuthLoginSerializer
        elif self.action == 'info':
            serializer_class = UserAuthInfoSerializer
        elif self.action == 'change_password':
            serializer_class = ChangePasswordSerializer
        elif self.action == 'logout':
            serializer_class = UserAuthLogoutSerializer
        return serializer_class

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            token_data = {
                'token': str(refresh.access_token),
                'refresh': str(refresh),
            }
            return Response(token_data)
        else:
            return Response('用户名或密码错误', status=403)

    @action(detail=False, methods=['get'])
    def info(self, request):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        RefreshToken.for_user(request.user)
        return Response('成功退出')

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        instance = request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not check_password(serializer.data.get('old_password'), instance.password):
                return Response('旧密码错误', status=400)
            instance.set_password(serializer.data.get('new_password2'))
            instance.save()
            return Response('密码重置成功')
        else:
            return Response(serializer.errors, status=400)
