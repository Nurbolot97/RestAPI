from rest_framework import generics
from .models import Company, Advertisement
from .serializers import *
from .pagination import *
from  rest_framework import filters
from  django_filters.rest_framework import DjangoFilterBackend



class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('company_name', 'address', 'owner__username')
    search_fields = ('company_name', 'address', 'owner__username')


class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer

    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update(
            {'owner': self.request.user}
        )
        return context


class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class AdvertisementView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = AdvertisementPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('company', 'title', 'body')
    search_fields = ('company', 'title', 'body')


class AdvertisementCreate(generics.CreateAPIView):
    serializer_class = AdvertisementCreateSerializer

    def get_serializer_context(self):
        context = super(AdvertisementCreate, self).get_serializer_context()
        return context


class AdvertisementDetail(generics.RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer
    lookup_field = 'pk'



