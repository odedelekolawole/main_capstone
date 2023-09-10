from rest_framework import serializers
from . models import Category1, Continent1, News1

class Category1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = "__all__"

class Continent1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Continent1
        fields = "__all__"

class News1Serializer(serializers.ModelSerializer):
    class Meta:
        model = News1
        fields = "__all__"
