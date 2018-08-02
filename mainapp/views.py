from django.shortcuts import render, reverse, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from . import models
from mainapp.models import Course, Section, CourseItem


def home(request):
    courses = Course.objects.all()
    sections = Section.objects.all()
    items = CourseItem.objects.all()
    context = {"courses": courses, "sections": sections, "items": items}
    return render(request, 'home.html', context)


def course(request, course_name):
    course = get_object_or_404(models.Course, url_endpoint__iexact=course_name)
    context = {"course": course}
    return render(request, '/{0}/'.format(course.title), context)


def section(request):
    pass


def item(request):
    pass

