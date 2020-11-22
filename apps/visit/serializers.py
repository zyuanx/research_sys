from rest_framework import serializers

from apps.visit.models import VisitList, VisitLocation
from utils.base_serializers import BaseModelSerializer


class VisitListSerializer(BaseModelSerializer):
    class Meta:
        model = VisitList
        fields = '__all__'


class VisitLocationSerializer(BaseModelSerializer):
    class Meta:
        model = VisitLocation
        fields = '__all__'
