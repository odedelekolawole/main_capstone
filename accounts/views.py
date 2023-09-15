from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# from . models import Category1, Continent1, News1
from . serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

"""
Additional
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class SignUpView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary="This endpoint signs up a user", operation_description="This endpoint signs up a user")
    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Success": "You have signed up successfully.",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    @swagger_auto_schema(operation_summary="This endpoint logs in a user", operation_description="This endpoint logs in a user")
    def post(self, request:Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = {
                "Success": f"Welcome { user.username.upper() } You are login successfully with { user.email }",
                "user_info": f"Kindly be reminded that you are logging in with the following details: USERNAME = { user }, USER_ID = { user.id }, with { user.email }. Kindly check your authentication token below",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"Message": "Ooops!...Something went wrong: Invalid Credentials"})


    @swagger_auto_schema(operation_summary="This endpoints provides the information of the user that is loggin", operation_description="This endpoints provides the information of the iuser that is loggin")
    def get(self, request:Request):
        details = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=details, status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="This endpoint logouts a user", operation_description="This endpoint logs out a user")
    def post(self, request):
        request.auth.delete()
        response = { "message": f"Bye-bye { request.user.username.upper() } You have been logged out successfully.",                        
        }
        return Response(data=response, status=status.HTTP_200_OK)