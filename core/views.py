from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    if request.method == "POST":
        from_city = request.POST.get('from_city')
        dest_city = request.POST.get('dest_city')
        depart_date = request.POST.get('depart_date')
        return_date = request.POST.get('return_date')
        passengers = request.POST.get('passengers')
        baggage = request.POST.get('baggage')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        additional_information = request.POST.get('additional_information')
        FlightBooking.objects.create(
            from_city=from_city, dest_city=dest_city, depart_date=depart_date, return_date=return_date, passengers=passengers, baggage=baggage, full_name=full_name, phone=phone, additional_information=additional_information)
        subject = "New Flight Booking from " + full_name
        message = "Flight Booking by" + " " + full_name + " " + "Depart From" + \
            " " + from_city + " " + "Destination" + " " + \
            dest_city + " " + "Phone" + " " + phone
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ybghartmagar@gmail.com',]
        send_mail(subject, message, from_email, recipient_list)

        messages.success(
            request, 'Your Flight Booking request sent successfully!')
        return redirect('index')

    sliders = Slider.objects.all()[:3]
    intro = AboutUs.objects.first()
    # tour_category = Tour_Type.objects.all()[:6]
    tour_category = Tour_Type.objects.all()[:6]
    destinations = Destination.objects.all()
    tours = Tour.objects.filter(is_featured=True)[:6]
    culturaltour = Tour.objects.filter(activity__name='Religious Tour')[:6]
    blogs = Blog.objects.all().order_by('-id')[:2]

    context = {
        'sliders': sliders,
        'intro': intro,
        'tour_category': tour_category,
        'destinations': destinations,
        'tours': tours,
        'culturaltour': culturaltour,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)


def tour_detail(request, tour_slug):
    single_tour = get_object_or_404(Tour, slug=tour_slug)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(name, email, phone, subject, message)
        Inquiry.objects.create(name=name, email=email, phone=phone,
                               message=message)
        messages.success(request, 'Your message sent successfully!')
        return redirect('/trips/' + single_tour.slug)
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(name, email, phone, subject, message)
        Inquiry.objects.create(name=name, email=email, phone=phone,
                               message=message)

        messages.success(request, 'Your message sent successfully!')
        subject = "Inquiry from " + name
        message = message + " " + "email " + " " + email + " " + "phone " + phone
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ybghartmagar@gmail.com',]
        send_mail(subject, message, from_email, recipient_list)

        return redirect('contact-us')
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


def booking_form(request):
    if request.method == 'GET':
        trip = request.GET.get('trip_name')
        price = request.GET.get('trip_price')
        # print(trip, price)

    if request.method == "POST":

        package = request.POST.get('package')
        price = request.POST.get('price')
        trip_start_date = request.POST.get('trip_start_date')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        nationality = request.POST.get('nationality')
        contact_number = request.POST.get('contact_number')
        emergency_contact_number = request.POST.get('emergency_contact_number')
        passport_no = request.POST.get('passport_no')
        place_of_issue = request.POST.get('place_of_issue')
        date_of_issue = request.POST.get('date_of_issue')
        date_of_expiry = request.POST.get('date_of_expiry')
        date_of_birth = request.POST.get('date_of_birth')
        no_of_people = request.POST.get('no_of_people')
        TourBooking.objects.create(
            package=package, price=price, trip_start_date=trip_start_date, full_name=full_name, email=email, nationality=nationality, contact_number=contact_number, emergency_contact_number=emergency_contact_number, passport_no=passport_no, place_of_issue=place_of_issue, date_of_issue=date_of_issue, date_of_expiry=date_of_expiry, date_of_birth=date_of_birth, no_of_people=no_of_people)
        subject = "New Flight Booking from " + full_name
        message = "New Tour Booking by" + " " + full_name + " " + "Tour Name" + \
            " " + package
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ybghartmagar@gmail.com',]
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'Booking Successful!')
        return redirect('booking-success')

    context = {
        'trip': trip,
        'price': price,

    }
    return render(request, 'booking-form.html', context)


def search(request):
    query = request.GET.get('tour-search')
    tours = Tour.objects.filter(name__icontains=query)
    context = {
        'tours': tours
    }
    return render(request, 'search.html', context)


def booking_success(request):
    return render(request, 'booking-success.html')
