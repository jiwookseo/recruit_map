# model
from django_filters import rest_framework as filters
from .models import Company, Job, Station, Route
from .serializers import CompanySerializer, JobSerializer, StationSerializer, RouteSerializer

# rest_framework
from rest_framework import viewsets, filters

# def-url-filters
from filters.mixins import FiltersMixin


class CompanyViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('start_salary', 'avg_salary', )
    ordering = ('id',)

    # add a mapping of query_params to db_columns(queries)
    filter_mappings = {
        'id': 'id',
        'name': 'name__icontains',
    }

    filter_value_transformations = {
        'taller_than': lambda val: val / 30.48  # cm to ft
    }


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
