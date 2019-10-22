# model
from .models import Company, Job, Station, Route
from .serializers import CompanySerializer, JobSerializer, StationSerializer, RouteSerializer
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CompaniesList(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompaniesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
