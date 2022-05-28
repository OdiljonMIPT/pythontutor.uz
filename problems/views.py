from django.shortcuts import render
from .models import Problem

def index(request):
    objs = Problem.objects.filter(is_published=True)
    context = {
        'problems': objs,
    }
    return render(request, 'problems/index.html', context)


def detail_lesson(request, slug):
    obj = Problem.objects.get(slug=slug)
    context = {
        'data': obj,
    }

    return render(request, 'problems/detail.html', context)
