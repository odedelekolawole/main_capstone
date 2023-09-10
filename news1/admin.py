from django.contrib import admin
from . models import Category1, Continent1, News1, Region1

# Register your models here.

class Category1Admin(admin.ModelAdmin):
    list_display = ["name", "tagline"]
    list_filter = ["name", "tagline"]
    list_editable = ["tagline"]

class Continent1Admin(admin.ModelAdmin):
    list_display = ["name"]

class News1Admin(admin.ModelAdmin):
    list_display = ["headline", "category", "reporter", "created"]
    list_filter = ["reporter", "category", "created"]
    list_editable = ["category"]

admin.site.register(Category1, Category1Admin)
admin.site.register(Continent1)
admin.site.register(News1, News1Admin)
admin.site.register(Region1)
