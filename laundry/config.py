from laundryadmin.models import Company

try:
    company = Company.objects.first()
    EMAIL_HOST_USER = company.comapny_email
    EMAIL_HOST_PASSWORD = company.password
except Company.DoesNotExist:
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''