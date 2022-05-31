from django.shortcuts import render
from lessons.models import Lesson


def home(request):
    objs = Lesson.objects.filter(is_published=True)
    context = {
        'lessons': objs,
    }
    return render(request, 'pages/home.html', context)


def about(request):

    return render(request, 'pages/about.html')
