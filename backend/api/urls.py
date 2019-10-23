from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'


router = DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('jobs', views.JobViewSet)
router.register('stations', views.StationViewSet)
router.register('routes', views.RouteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
