from rest_framework import generics, status, viewsets
from .models import Company, Advertisement
from .serializers import *
from .pagination import *
from  rest_framework import filters
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCompanyOwner


class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filterset_fields = ('company_name', 'address', 'owner__username')
    # search_fields = ('company_name', 'address', 'owner__username')

    def get_queryset(self):
        filter = self.request.query_params.get('filter')
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(company_name__icontains=filter)| Q(info__icontains=filter))
        return queryset


class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer
    permission_classes = [IsCompanyOwner,]
    http_method_names = ['put']

  
    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update(
            {'owner': self.request.user}
        )
        return context

class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class CompanyEditView(generics.UpdateAPIView):
    serializer_class = CompanyEditSerializer
    queryset = Company.objects.all()
    lookup_field = 'pk'
    http_method_names = ['patch',]
    

        
class AdvertisementView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('company__company_name', 'title')
    search_fields = ('company__company_name', 'title')
    

class AdvertisementCreate(generics.CreateAPIView):
    serializer_class = AdvertisementCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'OK'}, status=status.HTTP_201_CREATED, headers=headers)
        
        else:
            return Response({'You do not have permissions'}, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementDetail(generics.UpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementEditView(generics.RetrieveUpdateAPIView):
    serializer_class = AdvertisementEditSerializer
    queryset = Advertisement.objects.all()
    lookup_field = 'pk'
    http_method_names = ['patch',]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = CompanyImages.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')                # request.query_params = request.GET
        queryset = super().get_queryset()
        queryset = queryset.filter(description__icontains=q)
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





