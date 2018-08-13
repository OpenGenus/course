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
    course = get_object_or_404(models.Course, title__iexact=course_name)
    context = {"course": course}
    return render(request, 'course.html', context)


def section(request, course_name, section_name):
    section = models.Section.objects.filter(title=section_name)
    context = {"section": section}
    return render(request, 'section.html', context)


def item(request, course_name, section_name, item_name):
    item = models.CourseItem.objects.filter(title=item_name)
    context = {"item": item}
    return render(request, 'item.html', context)

