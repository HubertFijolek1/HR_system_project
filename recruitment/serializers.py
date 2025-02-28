from rest_framework import serializers
from .models import Candidate
from django.core.validators import validate_email

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
    
    def validate_email(self, value):
        value = value.lower()

        validate_email(value)

        return value
    
    def validate(self, data):
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("Both first name and last name are required.")
        return data