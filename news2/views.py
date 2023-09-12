from django.shortcuts import render
from django.http import HttpRequest
from . models import SliderNews, Category

# Create your views here.
def home(request):
    all_news = SliderNews.objects.all()
    all_category = Category.objects.all()
    first_four_news = SliderNews.objects.all()[:4]
    two_news = SliderNews.objects.all()[:2]
    news_count = SliderNews.objects.count()
    if news_count >= 2:
        last_two_news = SliderNews.objects.all()[news_count - 2:]
    else:
        last_two_news = SliderNews.objects.none()
    single_image = SliderNews.objects.all()[1]
    single_category = SliderNews.objects.all()[1]
    single_headline = SliderNews.objects.all()[1]
    single_content = SliderNews.objects.all()[1]
    single_date = SliderNews.objects.all()[1]

    single_image2 = SliderNews.objects.all()[2]
    single_category2 = SliderNews.objects.all()[2]
    single_headline2 = SliderNews.objects.all()[2]
    single_content2 = SliderNews.objects.all()[2]
    single_date2 = SliderNews.objects.all()[2]

    single_image3 = SliderNews.objects.all()[3]
    single_category3 = SliderNews.objects.all()[3]
    single_headline3 = SliderNews.objects.all()[3]
    single_content3 = SliderNews.objects.all()[3]
    single_date3 = SliderNews.objects.all()[3]

    single_image0 = SliderNews.objects.all()[0]
    single_category0 = SliderNews.objects.all()[0]
    single_headline0 = SliderNews.objects.all()[0]
    single_content0 = SliderNews.objects.all()[0]
    single_date0 = SliderNews.objects.all()[0]
    context = {
        "first_four_news": first_four_news,
        "categories": all_category,
        "two_news": two_news,
        "last_two_news": last_two_news,
        "single_image": single_image,
        "single_category": single_category,
        "single_headline": single_headline,
        "single_content": single_content,
        "single_date": single_date,

        "single_image2": single_image2,
        "single_category2": single_category2,
        "single_headline2": single_headline2,
        "single_content2": single_content2,
        "single_date2": single_date2,

        "single_image3": single_image3,
        "single_category3": single_category3,
        "single_headline3": single_headline3,
        "single_content3": single_content3,
        "single_date3": single_date3,

        "single_image0": single_image0,
        "single_category0": single_category0,
        "single_headline0": single_headline0,
        "single_content0": single_content0,
        "single_date0": single_date0,
    }
    return render(request, "news2/index.html", context)

def about(request):
    return render(request, "news2/about.html")

def category(request):
    return render(request, "news2/category.html")

def contact(request):
    return render(request, "news2/contact.html")
