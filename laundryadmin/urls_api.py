from django.urls import path
from .views_api import *

urlpatterns = [
    path('update/', Update_req),
    path('update-company/', UpdateCompany),
]