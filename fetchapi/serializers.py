from rest_framework import serializers
from . models import News2

class News2Serializer(serializers.ModelSerializer):
    class Meta:
        model = News2
        fields = "__all__"