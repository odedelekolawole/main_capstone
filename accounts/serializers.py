from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from . models import User
from drf_yasg.utils import swagger_auto_schema


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=8, write_only =True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    @swagger_auto_schema(operation_summary="This endpoint checks if the email provided by the user already exited in the database", operation_description="This endpoint checks if the email procuided by the user already exited in the database")
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email already been used")        
        return super().validate(attrs)

    @swagger_auto_schema(operation_summary="This endpoint hatches the password of the user and create toke for the user", operation_description="This endpoint hatches the password of the user and create toke for the user")
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
