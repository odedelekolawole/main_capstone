from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from . models import SliderNews, Category, NewsLetter, Enquiries
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        supplied_email = request.POST['email']
        if NewsLetter.objects.filter(email=supplied_email).exists():
            messages.info(request, f"Email already Used")
        else:
            NewsLetter.objects.create(email=supplied_email)
            messages.info(request, "Thanks for subscribing to our newsletter")
    all_news = SliderNews.objects.all()
    all_category = Category.objects.all()
    first_four_news = SliderNews.objects.all()[:4] # This is used to populate news with four divs not to disorganise
    two_news = SliderNews.objects.all()[:2] # This is used to populate news with two divs not to disorganise

    news_count = SliderNews.objects.count()
    if news_count >= 2: #conditional statement use for retrieve the late two news in the database if the number of news is not known
        last_two_news = SliderNews.objects.all()[news_count - 2:] #conditional statement use for retrieve the late two news in the database if the number of news is not known
    else:
        last_two_news = SliderNews.objects.none() #conditional statement use for retrieve the late two news in the database if the number of news is not known


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
        "all_news": all_news,
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
    if request.method == "POST":
        supplied_email = request.POST['email']
        if NewsLetter.objects.filter(email=supplied_email).exists():
            messages.info(request, f"Email already Used")
        else:
            NewsLetter.objects.create(email=supplied_email)
            messages.info(request, "Thanks for subscribing to our newsletter")
    all_news = SliderNews.objects.all()
    all_category = Category.objects.all()
    all_enquiries = Enquiries.objects.all()
    news_on_index_zero = SliderNews.objects.all()[0]
    news_on_index_one = SliderNews.objects.all()[1]
    news_on_index_two = SliderNews.objects.all()[2]
    news_on_index_three = SliderNews.objects.all()[3]
    news_on_index_four = SliderNews.objects.all()[4]
    context = {
        "all_news": all_news,
        "news_on_index_zero": news_on_index_zero,
        "news_on_index_one": news_on_index_one,
        "news_on_index_two": news_on_index_two,
        "news_on_index_three": news_on_index_three,
        "news_on_index_four": news_on_index_four,
        "all_category": all_category,
        "all_enquiries": all_enquiries,
    }
    return render(request, "news2/about.html", context)

def category(request):
    return render(request, "news2/category.html")

def contact(request):
    if request.method == "POST":
        supplied_name = request.POST["name"]
        supplied_email = request.POST["email"]
        supplied_phone = request.POST["phone"]
        supplied_subject = request.POST["subject"]
        supplied_information = request.POST["information"]
        Enquiries.objects.create(name=supplied_name, email=supplied_email, phone=supplied_phone, subject=supplied_subject, information=supplied_information)
        messages.info(request, "Informatio received")
    return render(request, "news2/contact.html")
