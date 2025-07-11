from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm, RegisterForm
from .models import Student


# Create your views here
def index(request):
    return render(request, 'index.html')
# #READ-DISPLAY ALL STUDENTWS
def student_list(request):
    students=Student.objects.all()
    return render(request, 'studentlist.html',{'students':students})

#CREATE-ADD NEW STUDENT
def add_student(request):
    form=StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'studentform.html',{'form':form})
#update-
def update_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'studentform.html',{'form':form})
#DELETE
def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')
#REGISTER NEW USERS
def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=RegisterForm()

    return render(request, 'register.html',{'form':form})