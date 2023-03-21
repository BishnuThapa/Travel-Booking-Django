from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def index(request):
    sliders = Slider.objects.all()[:3]
    tour_category = Tour_Type.objects.all()[:6]
    tours = Tour.objects.filter(is_featured=True)[:6]
    culturaltour = Tour.objects.filter(activity__name='Religious Tour')[:6]
    blogs = Blog.objects.all().order_by('-id')[:3]

    context = {
        'sliders': sliders,
        'tour_category': tour_category,
        'tours': tours,
        'culturaltour': culturaltour,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)


def tour_detail(request, tour_slug):
    single_tour = get_object_or_404(Tour, slug=tour_slug)
    context = {
        'single_tour': single_tour
    }
    return render(request, 'single-tour.html', context)
