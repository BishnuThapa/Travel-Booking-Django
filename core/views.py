from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
# Create your views here.


def index(request):
    sliders = Slider.objects.all()[:3]
    tour_category = Tour_Type.objects.all()[:6]
    tours = Tour.objects.filter(is_featured=True)[:6]
    culturaltour = Tour.objects.filter(activity__name='Religious Tour')[:6]
    blogs = Blog.objects.all().order_by('-id')[:2]

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


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    context = {
        'blogs': paged_blog
    }
    return render(request, 'blog.html', context)


def blog_detail(request, blog_slug):
    single_blog = get_object_or_404(Blog, slug=blog_slug)
    recent_blogs = Blog.objects.all().order_by('-id')[:3]
    featured_packages = Tour.objects.filter(is_featured=True)[:3]
    context = {
        'single_blog': single_blog,
        'recent_blogs': recent_blogs,
        'featured_packages': featured_packages
    }
    return render(request, 'blog-detail.html', context)


def contact(request):
    company_info = CompanyInfo.objects.first()
    context = {
        'company_info': company_info
    }
    return render(request, 'contact.html', context)
