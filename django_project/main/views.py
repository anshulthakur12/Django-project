from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, AccessRecord, WebPage
from . import forms
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html', {})


def registration_page(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            login(request, user)
            return render(request, 'main/index.html', {})
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'main/registrations.html', {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required()
def special(request):
    return HttpResponse("You are loged in, Nice! ")


@login_required()
def user_logout(request):
    logout(request)
    return render(request, 'main/index.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'main/index.html', {})
            else:
                return HttpResponse("Account Not Active")
        else:
            print('login failed')
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse("Request! Not found")
    else:
        return render(request, 'main/login.html', {})


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("ok")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request, 'main/forms_page.html', {'form': form})


def other_page(request):
    return render(request, 'main/other.html')




