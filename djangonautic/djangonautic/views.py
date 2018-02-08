# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def homepage(request):
#    return HttpResponse("Homepage")
    return render(request,"homepage.html")

def index_page(request):
#    return HttpResponse("Homepage")
    return render(request,"index.html")

def about(request):
#    return HttpResponse("about")
    return render(request,"about.html")

def services(request):
#    return HttpResponse("about")
    return render(request,"services.html")
