# model
from .models import Company, Job, Station, Route
from .serializers import CompanySerializer, JobSerializer, StationSerializer, RouteSerializer
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status, renderers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'companies': reverse('api:companies_list', request=request, format=format),
        # 'job': reverse('api:job_list', request=request, format=format),
        # 'station': reverse('api:station_list', request=request, format=format),
        # 'routes': reverse('api:routes_list', request=request, format=format),
    })


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
