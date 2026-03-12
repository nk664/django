from django.shortcuts import render

# Create your views here.
def student_home(request):
    
    students = ["nk", "pk", "dk"]
    
    data = {
        "student":students
        }

    return render(request, "student/student_home.html",data)