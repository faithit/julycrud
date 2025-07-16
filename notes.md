# Django Student CRUD Project

## 📁 templates/base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

## 📁 templates/students/student_list.html
```html
{% extends 'base.html' %}
{% block content %}
<h2 class="mb-4">Student List</h2>
<a href="{% url 'student_create' %}" class="btn btn-primary mb-3">Add Student</a>
<table class="table table-bordered">
  <thead class="table-dark">
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>Course</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {% for student in students %}
    <tr>
      <td>{{ student.full_name }}</td>
      <td>{{ student.age }}</td>
      <td>{{ student.course }}</td>
      <td>
        <a href="{% url 'student_update' student.id %}" class="btn btn-sm btn-warning">Edit</a>
        <a href="{% url 'student_delete' student.id %}" class="btn btn-sm btn-danger">Delete</a>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock %}
```

## 📁 templates/students/student_form.html
```html
{% extends 'base.html' %}
{% block content %}
<h2 class="mb-4">{% if form.instance.pk %}Edit{% else %}Add{% endif %} Student</h2>
<form method="POST" class="card card-body shadow-sm">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="btn btn-success">Save</button>
  <a href="{% url 'student_list' %}" class="btn btn-secondary">Back</a>
</form>
{% endblock %}
```

## 📁 students/models.py
```python
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - Age: {self.age}"
```

## 📁 students/forms.py
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'age', 'course']
```

## 📁 students/views.py
```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
```

## 📁 students/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
```

---

## 🧠 Explanations

**What is Django?**  
Django is a Python web framework that follows the MVT (Model-View-Template) pattern to build web applications quickly.

**MVT Pattern:**  
- **Model**: Handles the data (database structure)  
- **View**: Logic that connects the database and frontend  
- **Template**: Displays HTML with dynamic data

**What is a Model?**  
Defines your database table using Python classes. `Student` model stores name, age, and course.

**What is a View?**  
View functions handle the user requests and send data to templates.

**What is a Template?**  
HTML file with Django Template Language (DTL) to display dynamic content like `{{ student.name }}`.

**What is forms.py?**  
A place to define Django forms using `ModelForm`, which auto-generates form fields from a model.

**What is __str__()?**  
Defines how objects appear in admin or lists. Example: `return f"{self.full_name} - Age: {self.age}"`.

**GET vs POST:**  
- `GET`: Requests page or data (e.g., displaying a form)  
- `POST`: Submits form data (e.g., save student)  
We use `if request.method == 'POST':` to handle form submission.

**CSRF Token:**  
Prevents Cross Site Request Forgery. Always include `{% csrf_token %}` in forms.

**Django Admin Panel:**  
Create a superuser with `python manage.py createsuperuser`. Register models in `admin.py` to manage them visually.

**URLs:**  
Map user paths to views. For example:
```python
path('add/', views.student_create, name='student_create')
```
