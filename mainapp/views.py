from django.shortcuts import render, HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect


def home(request):
    return render(request, 'home.html')

