from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="adminlogin"),
    path('profile/', profile, name="profile"),
    path('change-password/',change_password, name='admin_change_password'),
    path('edit-price/', editprice, name="priceedit"),
    path('today-req/', todaywork, name="todaywork"),
    path('all-req/', allwork, name="allwork"),
    path('req-update/<uuid:id>/', req_update, name="req_update"),
    path('req-all-update/<uuid:id>/', req_all_update, name="req_all_update"),
    path('update-progress/<uuid:id>/', update_progress, name="update_progress"),
    path('update-all-progress/<uuid:id>/', update_all_progress, name="update_all_progress"),
    path('cancle-progress/<uuid:id>/', cancle_progress, name="cancle_progress"),
    path('cancle-all-progress/<uuid:id>/', cancle_all_progress, name="cancle_all_progress"),
    path('today-pickup-req/', today_pickup_req, name="pickup_today"),
    path('today-pickup-detials/<uuid:id>/', today_pickup_details, name="pickup_today_detials"),
    path('gen-setting/', gen_setting, name="gen_setting"),
]
