from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def student_home(request):
    
    students = Student.objects.filter(status = "Active")
    data = {
        "students": students
        }

    return render(request, "student/student_home.html",data)


def add_student(request):
    
   if request.method  == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")  
        

        Student.objects.create( 
        name =name,
        email = email,
        phone_number = phone_number
        )
        return redirect('student_home')

   return render(request,"student/add_student.html")

def delete_student(request, id):
    
    my_student = Student.objects.get(id = id)
    my_student.status = "Inactive"
    my_student.save()
    
    
    
    return redirect('student_home')
    

def update_student(request,id):
    student = Student.objects.get(id = id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone_number")
        
        student.save()
        
        return redirect("student_home")

    
    parameters ={
        "student": student
        }
    
    return render(request,"student/update.html",parameters)


