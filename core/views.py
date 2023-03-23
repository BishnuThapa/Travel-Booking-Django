from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
# Create your views here.


def index(request):
    sliders = Slider.objects.all()[:3]
    intro = AboutUs.objects.first()
    tour_category = Tour_Type.objects.all()[:6]
    tours = Tour.objects.filter(is_featured=True)[:6]
    culturaltour = Tour.objects.filter(activity__name='Religious Tour')[:6]
    blogs = Blog.objects.all().order_by('-id')[:2]

    context = {
        'sliders': sliders,
        'intro': intro,
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


def team(request):
    teamcat = TeamCategory.objects.all()
    teams = Team.objects.all().order_by('order')
    context = {
        'teamcat': teamcat,
        'teams': teams
    }
    return render(request, 'our-team.html', context)


def why_us(request):
    whyus = WhyUs.objects.all()
    context = {
        'whyus': whyus
    }
    return render(request, 'why-us.html', context)


def our_story(request):
    ourstory = OurStory.objects.first()
    context = {
        'ourstory': ourstory
    }
    return render(request, 'our-story.html', context)


def about_us(request):
    introduction = AboutUs.objects.first()
    context = {
        'introduction': introduction

    }
    return render(request, 'about-us.html', context)


# def destination(request):
#     # single_dest = get_object_or_404(Destination)
#     # context = {
#     #     'single_dest': single_dest,
#     # }
#     return render(request, 'destination.html')

def plan_my_trip(request):
    return render(request, 'plan-my-trip.html')


def offline_payment(request):
    return render(request, 'offline-payment.html')
