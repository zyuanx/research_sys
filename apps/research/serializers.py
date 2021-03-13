from apps.rbac.models import UserInfo
from apps.research.models import ResearchList, ResearchData
from utils.base_serializers import MongoBaseModelSerializer, BaseModelSerializer


class ResearchListSerializer(MongoBaseModelSerializer):
    class Meta:
        model = ResearchList
        fields = '__all__'


class ResearchDataSerializer(MongoBaseModelSerializer):
    class Meta:
        model = ResearchData
        fields = '__all__'


class UserInfoSerializer(BaseModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'nickname', 'email']
