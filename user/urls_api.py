from django.urls import path
from .views_api import *

urlpatterns = [
    path('register/', RegView),
    path('newreq/', NewRequestView)
]