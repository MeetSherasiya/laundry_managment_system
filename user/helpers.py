import string
import random
from django.conf import settings
from laundryadmin.models import Company
from django.core.mail import send_mail

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res

def send_mail_to_user(token, email):
    try:
        company = Company.objects.first()
        if not company:
            raise ValueError("Company object not found.")

        subject = "Your Account needs to be verified"
        message = f"Hi paste the link to verify account http://127.0.0.1:8000/verify/{token}"
        email_from = company.comapny_email
        settings.EMAIL_HOST_USER = email_from
        settings.EMAIL_HOST_PASSWORD = company.password
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        print(e)
        return False