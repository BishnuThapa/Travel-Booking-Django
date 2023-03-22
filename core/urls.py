
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog-detail'),
    path('trips/<slug:tour_slug>/', views.tour_detail, name='tour-detail'),
]
