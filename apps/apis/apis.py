from django.urls import path, include
from rest_framework import routers

import apps.users.views as user_views
import apps.research.views as research_views


router = routers.DefaultRouter()
router.register('user/register', user_views.UserRegisterViewSet, basename='register')
router.register('user/login', user_views.UserAuthViewSet, basename='login')
router.register('user/info', user_views.UserReadViewSet, basename='info')
router.register('user/logout', user_views.UserLogoutViewSet, basename='logout')
router.register('research/list', research_views.ResearchListViewSet, basename='research_list')
router.register('research/data', research_views.ResearchDataViewSet, basename='research_data')
router.register('research/export', research_views.ResearchExportViewSet, basename='research_export')

urlpatterns = [
    path('', include(router.urls)),
]
