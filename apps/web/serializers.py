from rest_framework import serializers

from apps.web.models import Customer, Payment


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Payment
        fields = '__all__'
