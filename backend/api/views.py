# python built-in module
import json
from datetime import datetime

# model
from .models import Company, Job, Station, Route
from .serializers import CompanySerializer, JobSerializer, StationSerializer, RouteSerializer

# rest_framework
from django_filters import rest_framework as filters
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.decorators import action

# def-url-filters
from filters.mixins import FiltersMixin


class CompanyViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('start_salary', 'avg_salary', )
    ordering = ('id',)
    filter_mappings = {
        'id': 'id',
        'name': 'name__icontains',
        'farther_east': 'lng__gt',
        'farther_west': 'lng__lt',
        'farther_north': 'lat__gt',
        'farther_south': 'lat__lt',
        'more_avg': 'avg_salary__gte',
        'less_avg': 'avg_salary__lte',
        'more_frs': 'start_salary__gte',
        'less_frs': 'start_salary__lte',
        'ind_code': 'ind_code__icontains',
        'scale': 'scale',
    }

    @action(detail=True)
    def jobs(self, request, pk):
        instance = self.get_object()
        jobs = instance.jobs.filter(close__gt=datetime.now())
        serializer = JobSerializer(
            jobs, many=True, context={'request': request})
        return Response({
            "link": {
                "url": reverse('api:company-jobs', args=[pk], request=request),
                "company": reverse('api:company-detail', args=[pk], request=request),
            },
            "results": serializer.data
        }, status=status.HTTP_200_OK)


class JobViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Job.objects.filter(close__gt=datetime.now())
    serializer_class = JobSerializer
    filter_mappings = {
        'id': 'id',
        'title': 'title__icontains',
        'open': 'open',
        'close': 'close',
    }


class StationViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('id',)
    filter_mappings = {
        'id': 'id',
        'name': 'name__icontains',
    }

    @action(detail=True)
    def routes(self, request, pk):
        instance = self.get_object()
        routes = instance.routes.all()
        serializer = RouteSerializer(
            routes, many=True, context={'request': request})
        return Response({
            "link": {
                "url": reverse('api:station-routes', args=[pk], request=request),
                "station": reverse('api:station-detail', args=[pk], request=request),
            },
            "results": serializer.data
        }, status=status.HTTP_200_OK)


class RouteViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('company',)
    filter_mappings = {
        'id': 'id',
        'station': 'station',
        'company': 'company',
    }

    def create(self, request, *args, **kwargs):
        is_json = isinstance(request.data, str)
        data = json.loads(request.data) if is_json else request.data
        serializer = self.get_serializer(data=data, many=is_json)
        serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
