
from django.urls import path
from student.views import student_home

urlpatterns = [
    path('std',student_home),
]