from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('image', ImageViewSet)


urlpatterns = [
    # Company end points
    path('company/list/', CompanyView.as_view(), name='company_list'),
    path('company/create/', CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('company/edit/<int:pk>/', CompanyEditView.as_view(), name='company_edit'),
    # Advertisement end points
    path('advertisement/list/', AdvertisementView.as_view(), name='advertisement_list'),
    path('advertisement/create/', AdvertisementCreate.as_view(), name='advertisement_create'),
    path('advertisement/<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('advertisement/edit/<int:pk>/', AdvertisementEditView.as_view(), name='advertisement_edit'),
    # Image router
    path('', include(router.urls))
]