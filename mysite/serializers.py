from rest_framework import serializers
from .models import *




class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'address', 'phone', 'info', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = instance.images.count()
        # representation['company'] = instance.company.company_name
        # representation['extra'] = 'Hello'
        return representation 


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'address', 'phone', 'info')
       

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'address', 'phone', 'info', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        # representation['company'] = instance.company.company_name
        # representation['extra'] = 'Hello'
        return representation        


class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'address', 'phone', 'info')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImages
        fields = ('image', 'description')

    
class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at', 'id')


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'body', 'image', 'company')


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'id')


class AdvertisementEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'body', 'image', 'company')