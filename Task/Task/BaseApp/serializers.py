from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import CRMLed, MASSlm

class CRMLedSerializer(serializers.ModelSerializer):
    # Add a detail_url field to CRMLedSerializer
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = CRMLed
        fields = '__all__'

    def get_detail_url(self, obj):
        # Generate the detail URL for CRMLed using reverse
        request = self.context.get('request')
        return reverse('crmled-detail', kwargs={'pk': obj.pk}, request=request)

class MASSlmSerializer(serializers.ModelSerializer):
    # Add a detail_url field to MASSlmSerializer
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = MASSlm
        fields = '__all__'

    def get_detail_url(self, obj):
        # Generate the detail URL for MASSlm using reverse
        request = self.context.get('request')
        return reverse('masslm-detail', kwargs={'pk': obj.pk}, request=request)
