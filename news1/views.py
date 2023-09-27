from django.shortcuts import render, get_object_or_404
from . models import Category1, News1
from . serializers import Category1Serializer, News1Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.http import Http404
import django_filters
from drf_yasg.utils import swagger_auto_schema
import uuid

# Create your views here.


"""
    STARTS: THIS ENDPOINT/VIEWS IS RESPONSIBLE FOR LISTING/DISPLAYING, POSTING, RETRIEVING, UPDATING AND DELETING CATEGORIES OF NEWS
"""

class Category1ListCreateView(APIView):
    serializer_class = Category1Serializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(operation_summary="This endpoint is responsible for listing all the categories of news in the database", operation_description="This are the list of all the categories of news")
    def get(self, request:Request, *args, **kwargs):
        paginator = self.pagination_class()
        category = Category1.objects.all().order_by("name")
        page = paginator.paginate_queryset(category, request)
        serializer = self.serializer_class(page, many=True)
        response = {
            "Success": f"Welcome '{ request.user.username.upper() }' This are all the news categories you can post a news to",
            "data": serializer.data
        }
        return paginator.get_paginated_response(data=response)
    
    
    @swagger_auto_schema(operation_summary="This endpoint is responsible for creating news category only by the superuser", operation_description="This endpoint create news category only by the superuser")
    def post(self, request:Request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            data = request.data
            serializer = Category1Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "Success": "Congratulations! Your news was posted successfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "Message": f"Unauthorized: You are logiing in as { request.user.username.upper() }, You are not authorized to post a news category because you can post nonsense category in our well-structured categories of news. Only staff can make this request. Thanks",
            }
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)
        
    
class Category1RetrieveUpdateDeleteView(APIView):
    permission_classes = []
    serializer_class = Category1Serializer

    @swagger_auto_schema(operation_summary="This endpoint is responsible for retrieving a category of news with UUID from the database by anyone", operation_description="This endpoint retrieves single category of news from the database with its UUID by anyone")
    def get(self, request, uuid):
        category = Category1.objects.get(id=uuid)
        serializer = self.serializer_class(category)        
        response = {
            "Success": f"Welcome { request.user.username.upper() } your news was retrieved successfully",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="This endpoint is responsible for updating or modifying news category only by the superuser", operation_description="This endpoint modifies or updates news category only by the superuser")
    def put(self, request, uuid):
        """
        STARTS: This endpoint is responsible for rupdating/modifying a category of news from the database.
        """
        category = get_object_or_404(Category1, id=uuid)
        user = request.user
        if user.is_superuser:
            data = request.data
            serializer = Category1Serializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                        "Success": "Weldone! The news category was updated successfully",
                "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "Message": f"Unauthorized: You are logging in as { request.user.username.upper() }, You are not authorized to update/modify a news category. Only staff can make this request. Thanks",
            }
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)


    @swagger_auto_schema(operation_summary="This endpoint is responsible for deleting news category only by the superuser", operation_description="This endpoint deleting news category only by the superuser")
    def delete(self, request, uuid):
        """
        STARTS: This endpoint is responsible for deleting/reoving a category of news from the database.
        """
        category = Category1.objects.get(id=uuid)
        user = request.user
        if user.is_superuser:
            category.delete()
            return Response(data={"Message": "The category of news was deleted succesfully"}, status=status.HTTP_410_GONE)
        else:
            response = {
                "Message": f"Unauthorized: You are logging in as { request.user.username.upper() }, You are not authorized to delete a news category. Only staff can make this request. Thanks",
            }
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)



"""
    ENDS: THE ENDPOINTS RESPONSIBLE FOR LISTING/DISPLAYING, POSTING, RETRIEVING, UPDATING AND DELETING CATEGORIES OF NEWS ENDS HERE
"""


"""
    BREAK BREAK BREAK BREAK BREAK NREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BREAK BRAEK
"""



class News1ListCreateView(APIView):
    permission_classes = [AllowAny]
    serializer_class = News1Serializer
    queryset = News1.objects.all()
    pagination_class = PageNumberPagination
    DjangoFilterBackend = [SearchFilter, OrderingFilter]
    ordering_fields = ["reporter"]
    search_fields = ['region', 'continent']
    

    @swagger_auto_schema(operation_summary="This endpoint is responsible for listing all the news in the database", operation_description="This are the list of all the news")
    def get(self, request):
        paginator = self.pagination_class()
        news = News1.objects.all().order_by("-created")
        page = paginator.paginate_queryset(news, request)
        serializer = self.serializer_class(page, many=True)
        message = {
            "Success": f"Welcome: '{ request.user.username.upper() }' you are accessing all the pages of our news here, enjoy your explore",
            "data": serializer.data
        }
        return paginator.get_paginated_response(data=message)
    
    @swagger_auto_schema(operation_summary="This endpoint is responsible for creating news by users", operation_description="This endpoint create news by users")
    def post(self, request):
            data = request.data
            serialized_data = self.serializer_class(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                response = {
                    "Success": f"Good job  '{  request.user.username.upper() }' Your news was posted successfully",
                    "User_Infomation": f"You are creating a news with the following details: USERNAME: { request.user.username }, with ID: { request.user.id }",
                    "data": serialized_data.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)    

    """
        This subsection is responsible responsible for for retrieving, updating/modifying, and deleting a news from the database
    """
class News1RetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = News1Serializer

    @swagger_auto_schema(operation_summary="This endpoint is responsible for retrieving news with its UUID from the database by anyone", operation_description="This endpoint retrieves single news from the database with its UUID by anyone")
    def get(self, request, uuid):
        """
            This endpoin is responsible for terieving/getting  news with UUID from the database 
        """
        news = News1.objects.get(id=uuid)
        serialized_data = self.serializer_class(instance=news)
        response = {
            "Kudos": f"Welcome The requested news was retrieved successfully by { request.user }",
            "data": serialized_data.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(operation_summary="This endpoint is responsible for updating or modifying news only by the creator of the news (reporter)", operation_description="This endpoint modifies or updates news only by the creator of the news (reporter)")
    def put(self, request, uuid):
        try:
            news = get_object_or_404(News1, id=uuid)
        except Http404:
            response = {
                "Message": "News not found, most likely you entered a wrong address"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        # Checks if the authenticated user is the owner of the news
        if request.user == news.reporter:
            data = request.data
            serialized_data = self.serializer_class(instance=news, data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                response = {
                    "Success": f"Welcome {news.reporter}. Your requested news to modify was updated successfully",
                    "data": serialized_data.data
                }
                return Response(data=response, status=status.HTTP_200_OK)  # Use 200 OK for successful updates

            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        # If the user is not the owner, return an unauthorized response
        response = {
            "message": f"UNAUTHORIZED! You are logging in as { request.user.username.upper() }. You cannot UPDATE/MODIFY this news because { news.reporter.username.upper() } is the author"
        }
        return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)


    @swagger_auto_schema(operation_summary="This endpoint is responsible for deleting news only by the creator of the news (reporter)", operation_description="This endpoint deleting news category only by the creator of the news (reporter)")
    def delete(self, request, uuid):
        news = get_object_or_404(News1, id=uuid)
        if request.user != news.reporter:
            response = {
                "Message": f"'FORBIDDEN': Hello { request.user.username.upper() }, you cannot delete the post the post belongs to { news.reporter.username.upper() }"
            }
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)
        else:
            news.delete()
            response = {
                "Message": f"News deleted successfully by { news.reporter.username.upper() }"
            }
            return Response(data=response, status=status.HTTP_410_GONE)
        

class GetReporterNewsOnly(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = News1Serializer

    @swagger_auto_schema(operation_summary="This list all the news associated with a particular user by passing the name on the url", operation_description="This list all the news associated with a particular user by passing the username on the url")
    def get(self, request, *args, **kwargs):
        user = request.user
        queryset = News1.objects.filter(reporter=user)
        serializer = self.serializer_class(queryset, many=True)
        response = {
            "Message": f"The are all the news posted by: { request.user.username.upper() }",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


class GetReporterNewsByparsingName(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = News1Serializer
    @swagger_auto_schema(operation_summary="This list all the news associated with a particular user", operation_description="This list all the news associated with a particular user")
    def get(self, request, *args, **kwargs):
        username = self.kwargs.get("username")
        queryset = News1.objects.filter(reporter__username=username)
        serializer = self.serializer_class(queryset, many=True)
        response = {
            "Message": f"The are all the news posted by you { username.upper() } ",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

"""
    ENDS: THE ENDPOINTS RESPONSIBLE FOR LISTING/DISPLAYING, POSTING, RETRIEVING, UPDATING AND DELETING MAIN NEWS ENDS HERE
"""
class News1Filter(django_filters.FilterSet):
    class Meta:
        model = News1
        fields = ["continent", "category"] 
