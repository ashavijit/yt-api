from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import CursorPagination

class YtVideosPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class YtVideosList(generics.ListAPIView):
    search_fields = ['titles', 'desc']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend ,filters.OrderingFilter)
    filter_fields = ['chnl_id', 'chnl_title']
    ordering= ('-publishersDate')
    queryset = YtVideos.objects.all()
    serializer_class = YtVideosSerializer
    pagination_class = YtVideosPagination