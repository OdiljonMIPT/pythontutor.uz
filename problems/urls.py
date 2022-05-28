from django.urls import path
from .views import index, detail_lesson

urlpatterns = [
    path('', index),
    path('<str:slug>/', detail_lesson)
]
