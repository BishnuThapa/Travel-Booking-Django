
from django.urls import path, include
from . import views
from .context_processor import destination, activities

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('plan-my-trip/', views.plan_my_trip, name='plan-my-trip'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog-detail'),
    path('trips/<slug:tour_slug>/', views.tour_detail, name='tour-detail'),
    path('destination/<slug:destination_slug>/',
         destination, name='destination'),
    path('activities/<slug:activity_slug>/',
         activities, name='activities'),
    path('team/', views.team, name='team'),
    path('booking-form/', views.booking_form, name='booking-form'),
    path('booking-success/', views.booking_success, name="booking-success"),
    path('why-us/', views.why_us, name='why-us'),
    path('our-story/', views.our_story, name='our-story'),
    path('about-us/', views.about_us, name='about-us'),
    path('offline-payment/', views.offline_payment, name='offline-payment'),
    path('search/', views.search, name='search'),
]
