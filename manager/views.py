from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from .forms import *
from . models import *
from . filters import *

# Create your views here.

def home(request):
    return render(request,'manager/home.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request,'manager/login.html')


@login_required(login_url='loginUser')
def dashboard(request):
    return render(request,'manager/dashboard.html')


@login_required(login_url='loginUser')
def logoutUser(request):
    logout(request)
    return render(request,'manager/login.html')


@login_required(login_url='loginUser')
def teachers(request):
    teacher = Teacher.objects.all()
    filter = TeacherFilter(request.POST,queryset = teacher)
    teacher = filter.qs

    context = {'teacher':teacher,'filter':filter}
    return render(request,'manager/teachers.html',context)


@login_required(login_url='loginUser')
def add_teacher(request):
    form = CreateTeacher()
    if request.method == 'POST':
        form = CreateTeacher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    context = {'form':form}
    return render(request,'manager/add_teacher.html',context)


@login_required(login_url='loginUser')
def update_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = CreateTeacher(instance=teacher)
    if request.method == 'POST':
        form = CreateTeacher(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    context = {'form':form}
    return render(request,'manager/update_teacher.html',context)


@login_required(login_url='loginUser')
def delete_teacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers')
    context = {'teacher':teacher}
    return render(request,'manager/delete_teacher.html',context)

@login_required(login_url='loginUser')
def students(request):
    student = Student.objects.all()
    filter = StudentFilter(request.POST,queryset = student)
    student = filter.qs
    context = {'student':student,'filter':filter}
    return render(request,'manager/students.html',context)

@login_required(login_url='loginUser')
def add_student(request):
    form = CreateStudent()
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form':form}
    return render(request,'manager/add_student.html',context)

@login_required(login_url='loginUser')
def update_student(request,pk):
    student = Student.objects.get(id=pk)
    form = CreateStudent(instance=student)
    if request.method == 'POST':
        form = CreateStudent(request.POST,instance=student)
        if form.is_valid():
            form.save();
            return redirect('students')
    context = {'form':form}
    return render(request,'manager/update_student.html',context)

@login_required(login_url='loginUser')
def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')
    context = {'student':student}
    return render(request,'manager/delete_student.html',context)

@login_required(login_url='loginUser')
def staffs(request):
    staff = Staff.objects.all()
    filter = StaffFilter(request.POST,queryset = staff)
    staff = filter.qs
    context = {'staff':staff,'filter':filter}
    return render(request,'manager/staffs.html',context)

@login_required(login_url='loginUser')
def add_staff(request):
    form = CreateStaff()
    if request.method == 'POST':
        form = CreateStaff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffs')
    context = {'form':form}
    return render(request,'manager/add_staff.html',context)

@login_required(login_url='loginUser')
def update_staff(request,pk):
    staff = Staff.objects.get(id=pk)
    form = CreateStaff(instance=staff)
    if request.method == 'POST':
        form = CreateStaff(request.POST,instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staffs')
    context = {'form':form}
    return render(request,'manager/update_staff.html',context)

@login_required(login_url='loginUser')
def delete_staff(request,pk):
    staff = Staff.objects.get(id=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staffs')
    context = {'staff':staff}
    return render(request,'manager/delete_staff.html',context)