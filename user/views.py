from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import *
from laundryadmin.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from laundryadmin.models import Price
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def userlogin(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.profile.is_verified:
                login(request, user)
                return redirect('index')
            else:
                error_message = "User is not verified. Please verify your account."
                return render(request, 'userlogin.html', {'messages': error_message})
        else:
            error_message = "Invalid username or password"
            return render(request, 'userlogin.html', {'messages': error_message})
    else:
        return render(request, 'userlogin.html')


def userregister(request):
    return render(request, 'userregister.html')

@login_required(login_url='/login/')
def index(request):
    if request.user:
        price = Price.objects.first()
        progress_counts = {}
        for progress_choice in UserReqeuest.PROGRESS_CHOICES:
            progress = progress_choice[0]
            count = UserReqeuest.objects.filter(user = request.user, progress=progress).count()
            progress_counts[progress] = count

        history = UserReqeuest.objects.filter(user = request.user).order_by('-pickup_date')
        context = {
            'progress_counts': progress_counts,
            'history': history,
            'price': price,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')

@login_required(login_url='/login/')
def new_request(request):
    return render(request, 'new_request.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/login/')

@login_required(login_url='/login/')
def user_profile(request):
    user = request.user
    context = {
        'users': user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('user_profile')
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

    return render(request, 'change_password.html', {'form': form})




class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_submitting'] = False
        return context

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(self.request, 'Email address not found.')
            return redirect(reverse_lazy('password-reset'))

        return super().form_valid(form)