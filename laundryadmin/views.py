from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from .models import *
from user.models import UserReqeuest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

today = date.today()

def is_superuser(user):
    return user.is_superuser


def login(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser or user.is_staff:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'You are not authorized to access this page.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'admin/login.html')

@login_required(login_url='/admin-site/login/')
def home(request):
    today_requests = UserReqeuest.objects.filter(created_at__date=today, progress = 'Pending').count()
    today_accept = UserReqeuest.objects.filter(created_at__date=today, progress = 'Accept').count()
    today_inprogress = UserReqeuest.objects.filter(created_at__date=today, progress = 'Inprogress').count()
    today_finish = UserReqeuest.objects.filter(created_at__date=today, progress = 'Finish').count()
    today_cancle = UserReqeuest.objects.filter(created_at__date=today, progress = 'Cancle').count()
    total_requests = UserReqeuest.objects.all().count()
    total_accept = UserReqeuest.objects.filter(progress = 'Accept').count()
    total_inprogress = UserReqeuest.objects.filter(progress = 'Inprogress').count()
    total_finish = UserReqeuest.objects.filter(progress = 'Finish').count()
    total_cancle = UserReqeuest.objects.filter(progress = 'Cancle').count()
    price = Price.objects.first()
    total_unpaids = UserReqeuest.objects.filter(payment='Unpaid')
    total_unpaid = 0
    for user in total_unpaids:
        if user.progress != 'Cancle':
            total_unpaid += user.totalprice

    total_cashs = UserReqeuest.objects.filter(payment='Cash')
    total_cash = 0
    for user in total_cashs:
        if user.progress != 'Cancle':
            total_cash += user.totalprice

    total_onlines = UserReqeuest.objects.filter(payment='Online')
    total_online = 0
    for user in total_onlines:
        if user.progress != 'Cancle':
            total_online += user.totalprice

    context = {
        'price' : price,
        'today_request': today_requests,
        'today_accept': today_accept,
        'today_inprogress': today_inprogress,
        'today_finish': today_finish,
        'today_cancle': today_cancle,
        'total_request': total_requests,
        'total_accept': total_accept,
        'total_inprogress': total_inprogress,
        'total_finish': total_finish,
        'total_cancle': total_cancle,
        'total_unpaid': total_unpaid,
        'total_cash': total_cash,
        'total_online': total_online,
    }
    return render(request, 'admin/admin.html', context)

@login_required(login_url='/admin-site/login/')
def profile(request):
    user = request.user
    context = {
        'users': user,
    }
    return render(request, 'admin/profile.html', context)

@login_required(login_url='/admin-site/login/')
def editprice(request):
    price = Price.objects.first()
    if request.method == "POST":
        topwear = request.POST.get('topwearprice')
        bottomwear = request.POST.get('bottomwearprice')
        woolenwear = request.POST.get('woolenwearprice')

        if price is None:
            Price.objects.create(topwear = topwear, bottomwear = bottomwear, woolenwear = woolenwear)
            return redirect('home')

        price.topwear = topwear
        price.bottomwear = bottomwear
        price.woolenwear = woolenwear
        price.save()
        return redirect('home')

@login_required(login_url='/admin-site/login/')
def todaywork(request):
    user = UserReqeuest.objects.filter(pickup_date=today).order_by('-pickup_date')
    context = {
        'page_obj': user,
    }
    return render(request, 'admin/today_work.html', context)

@login_required(login_url='/admin-site/login/')
def allwork(request):
    user = UserReqeuest.objects.all().order_by('-pickup_date')
    context = {
        'page_obj': user,
    }
    return render(request, 'admin/all_work.html', context)

@login_required(login_url='/admin-site/login/')
def req_update(request, id):
    user =  get_object_or_404(UserReqeuest, uuid=id)
    price = Price.objects.first()
    context = {
        'users': user,
        'prices': price
    }
    return render(request, 'admin/req_update.html', context)

@login_required(login_url='/admin-site/login/')
def req_all_update(request, id):
    user =  get_object_or_404(UserReqeuest, uuid=id)
    price = Price.objects.first()
    context = {
        'users': user,
        'prices': price
    }
    return render(request, 'admin/req_all_update.html', context)

@login_required(login_url='/admin-site/login/')
def update_req(requset):
    return render(requset, 'admin/today_work.html')


PROGRESS_MAPPING = {
    'Pending': 'Accept',
    'Accept': 'Inprogress',
    'Inprogress': 'Finish',
}

@login_required(login_url='/admin-site/login/')
def update_progress(request, id):
    user = get_object_or_404(UserReqeuest, uuid=id)
    current_progress = user.progress

    if current_progress in PROGRESS_MAPPING:
        next_progress = PROGRESS_MAPPING[current_progress]
        user.progress = next_progress
        user.save()

    return redirect('todaywork')

@login_required(login_url='/admin-site/login/')
def update_all_progress(request, id):
    user = get_object_or_404(UserReqeuest, uuid=id)
    current_progress = user.progress

    if current_progress in PROGRESS_MAPPING:
        next_progress = PROGRESS_MAPPING[current_progress]
        user.progress = next_progress
        user.save()

    return redirect('allwork')

@login_required(login_url='/admin-site/login/')
def cancle_progress(request, id):
    user = get_object_or_404(UserReqeuest, uuid=id)
    next_progress = 'Cancle'
    user.progress = next_progress
    user.save()
    return redirect('todaywork')

@login_required(login_url='/admin-site/login/')
def cancle_all_progress(request, id):
    user = get_object_or_404(UserReqeuest, uuid=id)
    next_progress = 'Cancle'
    user.progress = next_progress
    user.save()
    return redirect('allwork')

@login_required(login_url='/admin-site/login/')
def today_pickup_req(request):
    user = UserReqeuest.objects.filter(pickup_date=today, service_type='pickup').order_by('-pickup_date')
    context = {
        'users' : user,
    }
    return render(request, 'admin/today_pickup.html', context)

@login_required(login_url='/admin-site/login/')
def today_pickup_details(request, id):
    user = get_object_or_404(UserReqeuest, uuid=id)
    context = {
        'users' : user,
    }
    return render(request, 'admin/pickup_details.html', context)

@login_required(login_url='/admin-site/login/')
def gen_setting(request):
    company = Company.objects.first()
    context = {
        'company': company
    }
    return render(request, 'admin/gen_setting.html', context)

@login_required(login_url='/admin-site/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
        else:
            if 'old_password' in form.errors:
                messages.error(request, 'Enter Current Password Properly.')
            else:
                messages.error(request, 'New passwords Do Not Match.')

    else:
        form = PasswordChangeForm(request.user)

    form.fields['old_password'].widget.attrs['class'] = 'form-control'
    form.fields['new_password1'].widget.attrs['class'] = 'form-control'
    form.fields['new_password2'].widget.attrs['class'] = 'form-control'

    return render(request, 'admin/change_password.html', {'form': form})