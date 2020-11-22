from django.urls import path, include
from rest_framework import routers

import apps.users.views as user_views
import apps.research.views as research_views
import apps.visit.views as visit_views

router = routers.DefaultRouter()
router.register('user/register', user_views.UserRegisterViewSet)
router.register('user/login', user_views.UserAuthViewSet)
router.register('user/info', user_views.UserReadViewSet)
router.register('research/list', research_views.ResearchListViewSet, basename='research_list')
router.register('research/data', research_views.ResearchDataViewSet, basename='research_data')
router.register('research/export', research_views.ResearchExportViewSet, basename='research_export')
# router.register('visit/location', visit_views.VisitLocationViewSet)
# router.register('visit/list', visit_views.VisitListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
