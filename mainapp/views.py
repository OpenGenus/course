from django.shortcuts import render, HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def course(request):
    return render(request, 'course.html')


def section(request):
    return render(request, 'section.html')


def item(request):
    return render(request, 'item.html')
