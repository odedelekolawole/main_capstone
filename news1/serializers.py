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
    reporter_continent = serializers.SerializerMethodField("get_reporter_continent")
    reporter_region = serializers.SerializerMethodField("get_reporter_region")
    reporter_name = serializers.SerializerMethodField("get_reporter_name")
    class Meta:
        model = News1
        fields = ["id", "headline", "content", "image", "category", "reporter", "reporter_name", "continent", "reporter_continent", "region", "reporter_region", "photographer", "created"]

    def get_reporter_name(self, obj):
        return obj.reporter.username

    def get_reporter_continent(self, obj):
        return obj.continent.name
    
    def get_reporter_region(self, obj):
        return obj.region.name
