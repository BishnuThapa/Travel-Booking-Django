from core.models import Destination, CompanyInfo


def default(request):
    destination = Destination.objects.all()
    company_info = CompanyInfo.objects.first()
    return {
        'destination': destination,
        'company_info': company_info
    }
