from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'api'


router = DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('jobs', views.JobViewSet)
router.register('stations', views.StationViewSet)
router.register('routes', views.RouteViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Gil-Job-E API",
        default_version='v1',
        description="hypermedia-driven REST API with Django REST framework",
        contact=openapi.Contact(email="jiwookseo.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path("doc/", schema_view.with_ui('redoc', cache_timeout=0))
]
