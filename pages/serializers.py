from rest_framework import serializers
from .models import *
from django.conf import settings


class PageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageTypeModel
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContentModel
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = '__all__'
        
        
class WhoAreWeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoAreWeModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            image_path = instance.image.url
            full_image_url = f"{settings.BASE_URL}{image_path}" 
            data['image'] = full_image_url
        return data

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationModel
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            image_path = instance.image.url
            full_image_url = f"{settings.BASE_URL}{image_path}" 
            data['image'] = full_image_url
        return data


class ParentSerializer(serializers.Serializer):
    banner_data = BannerSerializer(many=True)
    who_are_we_data = WhoAreWeSerializer(many=True)
    certification_data = CertificationSerializer(many=True)