from django.shortcuts import render

def intermediateView(request):
    context = {}
    return render(request, 'intermediateViewHTML.html', context)