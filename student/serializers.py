from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Registration    

class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=100,
        error_messages={'required': 'Name is required',
                        'blank': 'Name is required'}
    )
    email = serializers.EmailField(
        error_messages={'required': 'Email is required',
                        'invalid': 'Enter a valid email address'}
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={'required': 'Password is required',
                        'blank': 'Password is required'}
    )

    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError("Length of password must be at least 8")
        return value;


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Registration.objects.create(**validated_data)



   