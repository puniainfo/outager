from rest_framework import serializers
from .models import *

class OutageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageModel
        fields = ['id','received_from', 'application_name', 'outage_start_time', 'outage_end_time','outage_time','outage_status']


