from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

def intermediateView(request):
    context = {}
    return render(request, 'intermediateViewHTML.html', context)

def basetemplate(request):
    context = {}
    return render(request, 'website_basetemplate.html', RequestContext(request))
