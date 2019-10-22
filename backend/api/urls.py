from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path("companies/",
         views.CompaniesList.as_view(), name="companies_list"),
    path("companies/<int:pk>/",
         views.CompaniesDetail.as_view(), name="companies_detail"),
    # path("jobs/",
    #      views.jobs_list, name="jobs_list"),
    # path("jobs/<int:id>/",
    #      views.jobs_detail, name="jobs_detail"),
    # path("stations/",
    #      views.stations_list, name="stations_list"),
    # path("stations/<int:id>/",
    #      views.stations_detail, name="stations_detail"),
    # path("routes/",
    #      views.routes_list, name="routes_list"),
    # path("routes/<int:station_id>/<int:company_id>/",
    #      views.routes_detail, name="routes_detail"),
]
