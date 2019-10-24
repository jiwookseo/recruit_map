from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if 'all' in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)
