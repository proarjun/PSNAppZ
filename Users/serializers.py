from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 15, min_length = 8, write_only = True)
    first_name = serializers.CharField(max_length=255, min_length = 2, write_only = True)
    last_name = serializers.CharField(max_length=255, min_length = 2, write_only = True)
    email = serializers.EmailField(max_length=255, write_only = True)
    password = serializers.CharField(max_length=255, min_length = 8, write_only = True)

    def validate(self, attrs):
        mail = attrs.get('email', '')
        if User.objects.filter(email = mail).exists():
            raise serializers.ValidationError({"email:Email ID already exists"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)