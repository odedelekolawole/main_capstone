from django.shortcuts import render, get_object_or_404
import requests
from . serializers import News2Serializer
from . models import News2
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_external_news(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=61b8cb52e787484388c5395e6f9c7596')
    response = requests.get(url)
    all_data = response.json()
    converted_data = dict(all_data)
    for single_news in converted_data["articles"]:
        news_author = single_news.get("author", "")
        news_title = single_news.get("title", "")
        news_description = single_news.get("description", "")
        news_url = single_news.get("url", "")
        news_image = single_news.get("urlToImage", "")
        news_created = single_news.get("publishedAt", "")
        news_content = single_news.get("content", "")
        News2.objects.create(author=news_author, title=news_title, description=news_description, url=news_url, image=news_image, published=news_created, content=news_content)
    database_news = News2.objects.all()
    serialized_news = News2Serializer(database_news, many=True)
    return Response(serialized_news.data, status=status.HTTP_200_OK)

def fetch_news(request):
    database_news = News2.objects.all()
    context = {
        "database_fetched_news": database_news
    }
    return render(request, 'fetchapi/fetch.html', context )
