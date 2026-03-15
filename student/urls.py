
from django.urls import path
from . import views

urlpatterns = [
    path('std/',views.student_home, name = "student_home"),
    path("add_student/",views.add_student, name = "add_student"),
    
    path("update_student/<int:id>/",views.update_student, name = 'update_student'),

    path("delete_student/<int:id>/", views.delete_student, name = 'delete_student')
    
    
]