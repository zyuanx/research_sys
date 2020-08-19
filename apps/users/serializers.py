from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.users.models import UserInfo
from utils.base_serializers import BaseModelSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户注册、添加序列化
    """
    password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('密码长度不应少于6个字符')
        return make_password(value)

    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'password']


class UserAuthSerializer(serializers.ModelSerializer):
    """
    用户认证序列化
    """

    class Meta:
        model = UserInfo
        fields = ['username', 'password']


class UserReadSerializer(BaseModelSerializer):
    """
    用户信息获取序列化
    """

    class Meta:
        model = UserInfo
        fields = ['id', 'nickname', 'avatar', 'username', 'created_time', 'modified_time']
