from django.urls import path, include
from rest_framework import routers

import apps.users.views
import apps.research.views

router = routers.DefaultRouter()
router.register('user/register', apps.users.views.UserRegisterViewSet)
router.register('user/login', apps.users.views.UserAuthViewSet)
router.register('user/info', apps.users.views.UserReadViewSet)
router.register('research/list', apps.research.views.ResearchListViewSet, basename='research_list')
router.register('research/data', apps.research.views.ResearchDataViewSet, basename='research_data')

urlpatterns = [
    path('', include(router.urls)),
]
