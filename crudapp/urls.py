from django.urls import path

from  .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentlist/',views.student_list,name='student_list'),
    path('add/',views.add_student,name='add_student'),
    path('edit/<int:pk>',views.update_student,name='update_student'),
    path('delete/<int:pk>',views.delete_student,name='delete_student'),
    path('register/',views.register, name='register')
]