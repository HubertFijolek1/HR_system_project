from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
    
    def validate_email(self, value):
        return value.lower()
    
    def validate(self, data):
        # Ensure both first_name and last_name are provided.
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("Both first name and last name are required.")
        return data