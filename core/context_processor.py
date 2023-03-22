from core.models import Destination, CompanyInfo, Tour_Type


def default(request):
    destination = Destination.objects.all()
    activities = Tour_Type.objects.all()
    company_info = CompanyInfo.objects.first()
    return {
        'destination': destination,
        'company_info': company_info,
        'activities': activities
    }
