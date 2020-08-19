from django.urls import path, include
from rest_framework import routers

import apps.users.views

router = routers.DefaultRouter()
router.register('user/register', apps.users.views.UserRegisterViewSet)
router.register('user/login', apps.users.views.UserAuthViewSet)
router.register('user/info', apps.users.views.UserReadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
