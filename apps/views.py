from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages

def dashboard(request,
              template="dashboard.html"):
    return render(request, template, {
    })
