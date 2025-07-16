# JulyCRUD Project

A simple Django CRUD application.

---

## 📚 Documentation & Guides

- [XAMPP Installation & Usage Guide for Linux](./XAMPP-guide.md)

---

## 🚀 Django Basics

Django is a high-level Python web framework for rapid development and clean, pragmatic design.

### Key Commands

```bash
# Start a new project
django-admin startproject myproject

# Run development server
python manage.py runserver

# Create new app
python manage.py startapp students

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Django Project Structure

- `manage.py`: Command-line utility for administrative tasks.
- `project_name/`: Project settings and configuration.
- `app_name/`: Application code (models, views, templates, etc.).

---

## 🔄 Django CRUD(Create, Read, Update, Delete) Example: Student Model

CRUD operations are fundamental in web applications for managing data.

### Student Model Example

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    enrollment_date = models.DateField()
```

### Basic CRUD Views Example

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    # handle form submission for creation
    pass

def student_update(request, pk):
    # handle form submission for update
    pass

def student_delete(request, pk):
    # handle deletion
    pass
```

### Student Model Migration

```bash
python manage.py makemigrations students
python manage.py migrate
```

---

## 📝 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [XAMPP Installation & Usage Guide](./XAMPP-guide.md)

---
