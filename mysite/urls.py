from django.urls import path
from .views import *


urlpatterns = [
    path('list/', CompanyView.as_view(), name='company_list'),
    path('create/', CompanyCreate.as_view(), name='company_create'),
    path('<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('advertisement/', AdvertisementView.as_view(), name='advertisement_list'),
    path('advertisement/create/', AdvertisementCreate.as_view(), name='advertisement_create'),
    path('advertisement/<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
]