from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
    
        # Ensure the email is in lowercase
        value = value.lower()
        # Use Django's built-in email validator
        validate_email(value)
        # Optional: enforce a specific domain (for example, only allow company emails)
        # Uncomment below lines if needed:
        # if not re.match(r".+@company\.com$", value):
        #     raise serializers.ValidationError("Email must be a company email address.")
        return value
    
    def validate(self, data):
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("Both first name and last name are required.")
        return data