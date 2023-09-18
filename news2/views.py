from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from . models import SliderNews, Category, NewsLetter, Enquiries
from django.contrib import messages
from fetchapi.models import News2
import random

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
    sixth_news = SliderNews.objects.all()[6]
    seventh_news = SliderNews.objects.all()[6]
    eighth_news = SliderNews.objects.all()[7]
    ninth_news = SliderNews.objects.all()[8]
    tenth_news = SliderNews.objects.all()[9]
    eleventh_news = SliderNews.objects.all()[10]
    twelve_news = SliderNews.objects.all()[11]
    thirthenth_news = SliderNews.objects.all()[12]
    fourteenth_news = SliderNews.objects.all()[13]
    fifteenth_news = SliderNews.objects.all()[14]
    sixteeth_news = SliderNews.objects.all()[15]
    seventeenth_news = SliderNews.objects.all()[16]
    eighteenth_news = SliderNews.objects.all()[17]
    nineteenth_news = SliderNews.objects.all()[18]
    select_news0 = SliderNews.objects.filter(category=0)
    select_news1 = SliderNews.objects.filter(category=1)
    select_news2 = SliderNews.objects.filter(category=2)
    select_news3 = SliderNews.objects.filter(category=3)
    select_news4 = SliderNews.objects.filter(category=4)
    select_news5 = SliderNews.objects.filter(category=5)
    select_news6 = SliderNews.objects.filter(category=6)
    select_news7 = SliderNews.objects.filter(category=7)
    select_news8 = SliderNews.objects.filter(category=8)
    select_news9 = SliderNews.objects.filter(category=9)
    select_news10 = SliderNews.objects.filter(category=10)
    select_news11 = SliderNews.objects.filter(category=11)
    select_news12 = SliderNews.objects.filter(category=12)
    select_news13 = SliderNews.objects.filter(category=13)
    select_news14 = SliderNews.objects.filter(category=14)
    select_news15 = SliderNews.objects.filter(category=15)
    select_news16 = SliderNews.objects.filter(category=16)
    select_news17 = SliderNews.objects.filter(category=17)
    select_news18 = SliderNews.objects.filter(category=18)
    select_news19 = SliderNews.objects.filter(category=19)
    select_news20 = SliderNews.objects.filter(category=20)
    select_news21 = SliderNews.objects.filter(category=21)
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

def details(request, pk):
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
    return render(request, "news2/details.html", context)

    

def category(request):
    if request.method == "POST":
        supplied_email = request.POST['email']
        if NewsLetter.objects.filter(email=supplied_email).exists():
            messages.info(request, f"Email already Used")
        else:
            NewsLetter.objects.create(email=supplied_email)
            messages.info(request, "Thanks for subscribing to our newsletter")

    news_count = SliderNews.objects.count()
    if news_count >= 2: 
        last_two_news = SliderNews.objects.all()[news_count - 2:] 
    else:
        last_two_news = SliderNews.objects.none()
        
    all_news = SliderNews.objects.all()
    all_category = Category.objects.all()
    first_two_news = SliderNews.objects.all()[0:2]
    third_news = SliderNews.objects.all()[2]
    fourth_news = SliderNews.objects.all()[3]
    fifth_news = SliderNews.objects.all()[1:3]
    middle_news = SliderNews.objects.all()[5:7]
    sixth_news = SliderNews.objects.all()[3:5]
    sixth_seveth = SliderNews.objects.all()[6:8]
    seventh_news = SliderNews.objects.all()[7]
    context = {
        "all_news": all_news,
        "all_category": all_category,
        "first_two_news": first_two_news,
        "last_two_news": last_two_news,
        "third_news": third_news,
        "fourth_news": fourth_news,
        "fifth_news": fifth_news,
        "middle_news": middle_news,
        "sixth_news": sixth_news,
        "sixth_seveth": sixth_seveth,
        "seventh_news": seventh_news
    }
    return render(request, "news2/category.html", context)

# def category(request):
#     categories = Category.objects.all()
#     random_news_by_category = {}
#     for category in categories:
#         news_in_category = SliderNews.objects.filter(category=category)
#         if news_in_category.exists():
#             random_news_item = random.choice(news_in_category)
#             random_news_by_category[category.category] = random_news_item
#     print(random_news_by_category)
#     return render(request, 'news2/category.html', {'random_news_by_category': random_news_by_category},)




def contact(request):
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
    context = {
        "all_news": all_news,
        "all_category": all_category,
    }
    return render(request, "news2/contact.html", context)