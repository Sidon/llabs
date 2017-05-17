from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog
from .models import Person
from .serializers import PersonSerializer, TrackSerializer
from .util import get_face_person


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
    )
    permission_classes = (
         permissions.IsAuthenticated,
    )

    # authentication_classes = ()
    # permission_classes = ()

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class PersonViewSet(DefaultsMixin, LoggingMixin, viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    search_fields = ('name','facebookId', )
    ordering_fields = ('facebookId', 'name', 'gender',)
    queryset = Person.objects.all()


    def get_queryset(self):
        queryset = Person.objects.all()
        fb_id = self.request.query_params.get('facebookId', None)
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)
        empty = self.request.query_params.get('empty', None)


        if fb_id is not None:
            return queryset.filter(facebookId=fb_id)
        elif limit is not None:
            return queryset[:int(limit)]
        elif last is not None:
            return queryset.order_by('-facebookId')[:int(last)]

        return queryset

    def perform_create(self, serializer):
        if bool(self.request.POST):
            data_face = get_face_person(self.request.data['facebookId'])
            if bool(self.request.POST):
                serializer.save (
                    name = data_face['name'],
                    gender = data_face['gender'],
                    email = data_face['email']
                )



class TrackingViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializer
    search_fields = ('user','host', )
    queryset = APIRequestLog.objects.all()


    def get_queryset(self):
        queryset = APIRequestLog.objects.all()
        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        return queryset

