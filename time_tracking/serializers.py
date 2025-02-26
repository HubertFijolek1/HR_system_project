from rest_framework import serializers
from .models import TimeEntry

class TimeEntrySerializer(serializers.ModelSerializer):
    clock_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    clock_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, allow_null=True)
    
    class Meta:
        model = TimeEntry
        fields = "__all__"