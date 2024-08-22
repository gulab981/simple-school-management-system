from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginUser',views.loginUser,name='loginUser'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('teachers',views.teachers,name='teachers'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('update_teacher/<str:pk>/',views.update_teacher,name='update_teacher'),
    path('delete_teacher/<str:pk>/',views.delete_teacher,name='delete_teacher'),
    path('students',views.students,name='students'),
    path('add_student',views.add_student,name='add_student'),
    path('update_student/<str:pk>/',views.update_student,name='update_student'),
    path('delete_student/<str:pk>/',views.delete_student,name='delete_student'),
    path('staffs',views.staffs,name='staffs'),
    path('add_staff',views.add_staff,name='add_staff'),
    path('update_staff/<str:pk>/',views.update_staff,name='update_staff'),
    path('delete_staff/<str:pk>/',views.delete_staff,name='delete_staff'),
]
