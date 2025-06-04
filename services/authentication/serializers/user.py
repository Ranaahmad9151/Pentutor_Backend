from rest_framework import serializers
from ..models.user import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 
                 'profile_picture', 'phone_number', 'date_of_birth', 
                 'is_email_verified', 'created_at')
        read_only_fields = ('id', 'email', 'is_email_verified', 'created_at')