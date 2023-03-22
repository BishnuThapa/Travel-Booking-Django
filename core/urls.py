
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog-detail'),
    path('trips/<slug:tour_slug>/', views.tour_detail, name='tour-detail'),
    path('team/', views.team, name='team'),
    path('why-us/', views.why_us, name='why-us'),
    path('our-story/', views.our_story, name='our-story'),
    path('about-us/', views.about_us, name='about-us'),
]
