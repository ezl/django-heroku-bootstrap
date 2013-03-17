import os
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import login as auth_login_view
from django.contrib.auth.forms import UserCreationForm


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
            # return HttpResponseRedirect("/")

    return render(request, template, {
        'form': form,
    })

def login(request):
    extra_context = []
    return auth_login_view(request, extra_context=extra_context)
