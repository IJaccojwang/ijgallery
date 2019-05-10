from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image


def home(request):
    images = Image.all_images()
    return render(request, 'home.html', {"images": images})

def category(request, cat):
    category = cat
    images = Image.filter_by_category(category)
    return render(request,'category.html',{"images":images, "category":category})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})