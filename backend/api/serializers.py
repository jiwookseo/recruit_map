from rest_framework import serializers
from .models import Company, Job, Station, Route


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ("id",
                  "name",
                  "href",
                  "saramin_url",
                  "avg_salary",
                  "start_salary",
                  "address",
                  "lat",
                  "lng",
                  "ind_code",
                  "ind_array",
                  "place_id",
                  "ind_name",
                  "ind_key_code",
                  "ind_key_array",
                  "jobs_count",
                  )
        read_only_fields = ('ind_array', 'ind_key_array')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"
