from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Company, Job, Station, Route


class CompanySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:company-detail', lookup_field='pk')
    jobs = serializers.SerializerMethodField()

    def get_jobs(self, obj):
        return 'http://{}/api/companies/{}/jobs/'.format(self.context['request'].META['HTTP_HOST'], obj.id)

    class Meta:
        model = Company
        fields = (
            'id',
            'url',
            'jobs',
            'name',
            'href',
            'scale',
            'saramin_url',
            'avg_salary',
            'start_salary',
            'address',
            'lat',
            'lng',
            'ind_code',
            'ind_array',
            'place_id',
            'ind_name',
            'ind_key_code',
            'ind_key_array',
            'jobs_count',
        )
        read_only_fields = ('jobs', 'ind_array', 'ind_key_array',)


class CompanyField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return reverse('api:company-detail', args=(value.pk,), request=self.context['request'])


class JobSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:job-detail', lookup_field='pk')
    company = CompanyField(queryset=Company.objects.all())

    class Meta:
        model = Job
        fields = '__all__'


class StationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:station-detail', lookup_field='pk')
    routes = serializers.SerializerMethodField()

    def get_routes(self, obj):
        return 'http://{}/api/stations/{}/routes/'.format(self.context['request'].META['HTTP_HOST'], obj.id)

    class Meta:
        model = Station
        fields = (
            'id',
            'url',
            'routes',
            'name',
            'line',
            'address',
            'lat',
            'lng',
            'place_id',
        )
        read_only_fields = (
            'routes',
        )


class StationField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return reverse('api:station-detail', args=(value.pk,), request=self.context['request'])


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:route-detail', lookup_field='pk')
    company = CompanyField(queryset=Company.objects.all())
    station = StationField(queryset=Station.objects.all())

    class Meta:
        model = Route
        fields = (
            'id',
            'url',
            'company',
            'station',
            'time',
        )
