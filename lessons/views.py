from django.shortcuts import render
from .models import Lesson

def index(request):
    return render(request, 'lessons/index.html')


def detail_lesson(request, slug):
    obj = Lesson.objects.get(slug=slug)
    context = {
        'data': obj,
    }

    return render(request, 'lessons/detail.html', context)
