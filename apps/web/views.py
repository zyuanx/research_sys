from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from utils.rbac_permission import RbacPermission
from apps.web.models import Customer, Payment
from apps.web.serializers import CustomerSerializer, PaymentSerializer


class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, RbacPermission]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_prefix = 'customer'


class PaymentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, RbacPermission]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_prefix = 'payment'
