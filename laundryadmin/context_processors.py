from .models import Company

def company_logo(request):
    try:
        company = Company.objects.first()
        name = company.comapny_name
        logo = company.logo.url if company.logo else None
        fav_icon = company.fav_icon.url if company.fav_icon else None
    except Company.DoesNotExist:
        name = 'laundry'
        logo = None
        fav_icon = None

    return {'company_logo': logo, 'company_fav_icon': fav_icon, 'company_name': name}
