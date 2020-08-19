from apps.research.models import ResearchList, ResearchData
from utils.base_serializers import MongoBaseModelSerializer


class ResearchListSerializer(MongoBaseModelSerializer):
    class Meta:
        model = ResearchList
        fields = '__all__'


class ResearchDataSerializer(MongoBaseModelSerializer):
    class Meta:
        model = ResearchData
        fields = '__all__'
