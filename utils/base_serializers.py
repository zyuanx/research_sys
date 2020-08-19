from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer


class BaseModelSerializer(serializers.ModelSerializer):
    """
    序列化基类
    """
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    modified_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)


class MongoBaseModelSerializer(DocumentSerializer):
    """
    序列化基类
    """
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    modified_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
