from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

import course
from .forms import *
from .models import *


# Create your views here.

def index(request):
    is_succes = False
    review = Review.objects.all()
    courses = Course.objects.all()
    teacher = Teacher.objects.all()
    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('course:index')
    form = ReviewForm()
    return render(request, 'index.html', {
        'is_succes': is_succes,
        'teacher': teacher,
        'form': form,
        'courses': courses,
        'reviews': review,
    })


def more(request, slug):
    detail_course = get_object_or_404(Course, slug=slug)
    form = ApplicationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.course = detail_course
        instance.save()
        form = ApplicationForm()
        return redirect('course:index')
    return render(request, 'more.html',
                  {
                      'form': form,
                      'course': course,
                      'detail_course': detail_course,
                  })


def about(request, slug):
    teach = get_object_or_404(Teacher, slug=slug)
    is_succes = True
    return render(request, 'about.html', {
        'teach': teach,
        "is_succes": is_succes,
    })
