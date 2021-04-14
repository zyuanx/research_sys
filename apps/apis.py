from django.urls import path, include
from rest_framework import routers

import apps.rbac.views as rbac_views
import apps.research.views as research_views

router = routers.DefaultRouter()
router.register('auth', rbac_views.UserAuthViewSet, basename="auth")
router.register('user', rbac_views.UserViewSet, basename="user")
router.register('permission', rbac_views.PermissionViewSet, basename="permission")
router.register('role', rbac_views.RoleViewSet, basename="role")


router.register('research/list', research_views.ResearchListViewSet, basename='research_list')
router.register('research/data', research_views.ResearchDataViewSet, basename='research_data')
router.register('research/export', research_views.ResearchExportViewSet, basename='research_export')

urlpatterns = [
    path('', include(router.urls)),
]
