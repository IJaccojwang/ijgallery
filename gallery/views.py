from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image


def home(request):
    images = Image.all_images()
    return render(request, 'home.html', {"images": images})

def category(request, category):
    images = Image.filter_by_category(category)
    return render(request, 'category.html', {"images": images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        searched = request.GET.get("image")
        images = Image.search_image(searched)
        message = f"{searched}"

        return render(request, 'search.html', {"message":message,"images": images})
    else:
        message = "You haven't searched for any term"
        
        return render(request, 'search.html',{"message":message})