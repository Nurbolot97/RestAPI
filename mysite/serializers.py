from rest_framework import serializers
from .models import *



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'logo', 'address', 'phone', 'info')

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at')


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at')

    def create(self, validated_data):
        advertisement = Advertisement.objects.create(**validated_data)
        advertisement.save()
        return advertisement


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at')