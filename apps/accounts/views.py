import os
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import login as auth_login_view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from forms import UserProfileForm
from models import UserProfile


def signup(request,
           formclass=UserCreationForm,
           template="registration/signup.html"):
    form = formclass()
    if request.method == "POST":
        form = formclass(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=form.cleaned_data.get("password1"))
            auth_login(request, user)
            msg = "You have created an account!"
            messages.success(request, msg)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    return render(request, template, {
        'form': form,
    })

def login(request):
    extra_context = []
    return auth_login_view(request, extra_context=extra_context)

@login_required
def user_settings(request,
             formclass=UserProfileForm,
             template="accounts/user_settings.html"):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = formclass(instance=profile)
    if request.method == "POST":
        form = formclass(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            msg = "Success!"
            messages.success(request, msg)
            return HttpResponseRedirect(reverse("settings"))

    return render(request, template, {
        'form': form,
    })

