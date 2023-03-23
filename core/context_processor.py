from core.models import Destination, CompanyInfo, Tour_Type, Tour
from django.shortcuts import render, get_object_or_404


def default(request):
    destination = Destination.objects.all()
    activities = Tour_Type.objects.all()
    company_info = CompanyInfo.objects.first()
    return {
        'destination': destination,
        'company_info': company_info,
        'activities': activities
    }


def destination(request, destination_slug):
    tours = Tour.objects.filter(destination__name=destination_slug)
    single_dest = get_object_or_404(Destination, slug=destination_slug)
    context = {
        'single_dest': single_dest,
        'tours': tours,
    }
    return render(request, 'destination.html', context)
