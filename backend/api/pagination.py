from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if 'all' in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'url': "http://{}{}".format(self.request.META["HTTP_HOST"], self.request.path),
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.count,
            'results': data
        })


# class CustomPagination(LimitOffsetPagination):
#     def paginate_queryset(self, queryset, request, view=None):
#         if 'all' in request.query_params:
#             return None

#         return super().paginate_queryset(queryset, request, view)
