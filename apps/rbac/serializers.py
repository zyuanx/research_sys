from rest_framework import serializers

from apps.rbac.models import UserInfo, Permission, Role
from utils.base_serializers import BaseModelSerializer


class PermissionSerializer(BaseModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(BaseModelSerializer):
    title = serializers.CharField(required=True)

    # def validate_title(self, title):
    #     if len(title)<100:
    #         raise serializers.ValidationError('角色名不能为空')
    #     if not title:
    #         raise serializers.ValidationError('角色名不能为空')
    #     return title

    class Meta:
        model = Role
        fields = '__all__'


class UserInfoSerializer(BaseModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'nickname', 'email', 'avatar', 'roles', 'create_time', 'update_time']


class UserBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = []


class PasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'error': '两次密码输入不一致'})
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError({'error': '两次密码输入不一致'})
        return attrs

    def create(self, validated_data):
        user = UserInfo(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserInfo(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserAuthLoginSerializer(serializers.ModelSerializer):
    """
    auth 登录
    """
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = UserInfo
        fields = ['username', 'password']


class UserAuthInfoSerializer(serializers.ModelSerializer):
    """
    auth 信息获取
    """
    roles = serializers.StringRelatedField(many=True)
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        perms = obj.roles.values('permissions__method').distinct()
        return [p['permissions__method'] for p in perms]

    class Meta:
        model = UserInfo
        fields = ['nickname', 'username', 'email', 'avatar', 'permissions', 'roles', ]


class UserAuthLogoutSerializer(serializers.ModelSerializer):
    """
    auth 退出
    """

    class Meta:
        model = UserInfo
        fields = []
