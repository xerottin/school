from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

import course
from .forms import *
from .models import *


# Create your views here.

def index(request):
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
        'teacher': teacher,
        'form': form,
        'courses': courses,
        'reviews': review,
    })


def more(request, slug):
    detail_course = get_object_or_404(Course, slug=slug)
    form = ApplicationForm(request.POST or None)
    is_success = False
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        is_success = True
        instance.course = detail_course
        instance.save()
        form = ApplicationForm()
        return redirect('course:index')
    return render(request, 'more.html',
                  {
                      'form': form,
                      'is_success': is_success,
                      'course': course,
                      'detail_course': detail_course,
                  })


def about(request, slug):
    teach = get_object_or_404(Teacher, slug=slug)
    is_success = False
    return render(request, 'about.html', {
        'teach': teach,
        "is_success": is_success
    })
