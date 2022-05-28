from django.shortcuts import render
from .models import Lesson
from problems.models import Problem

def index(request):
    return render(request, 'lessons/index.html')


def detail_lesson(request, slug):
    obj = Lesson.objects.get(slug=slug)
    prb = Problem.objects.filter(cat=obj)
    context = {
        'data': obj,
        'problems': prb
    }

    return render(request, 'lessons/detail.html', context)
