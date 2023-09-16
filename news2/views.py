from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from . models import SliderNews, Category, NewsLetter, Enquiries
from django.contrib import messages
from fetchapi.models import News2

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
    first_news = SliderNews.objects.all()[0]
    second_news = SliderNews.objects.all()[1]
    third_news = SliderNews.objects.all()[2]
    fourth_news = SliderNews.objects.all()[3]
    fifth_news = SliderNews.objects.all()[4]
    sixth_news = SliderNews.objects.all()[5]
    first_four_news = SliderNews.objects.all()[:4]

    news_count = SliderNews.objects.count()
    if news_count >= 2: 
        last_two_news = SliderNews.objects.all()[news_count - 2:] 
    else:
        last_two_news = SliderNews.objects.none()


    if news_count >= 2: 
        first_two_news = SliderNews.objects.all()[news_count :2] 
    else:
        first_two_news = SliderNews.objects.none()


    context = {
        "all_news": all_news,
        "all_categories": all_category,
        "first_four_news": first_four_news,
        "first_news": first_news,
        "second_news": second_news,
        "third_news": third_news,
        "fourth_news": fourth_news,
        "fifth_news": fifth_news,
        "sixth_news": sixth_news,
        "last_two_news": last_two_news,
        "first_two_news": first_two_news,
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
    
    if request.method == "POST":
        supplied_name = request.POST["name"]
        supplied_email = request.POST["email"]
        supplied_phone = request.POST["phone"]
        supplied_subject = request.POST["subject"]
        supplied_information = request.POST["information"]
        Enquiries.objects.create(name=supplied_name, email=supplied_email, phone=supplied_phone, subject=supplied_subject, information=supplied_information)
        messages.info(request, "Informatio received")

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


