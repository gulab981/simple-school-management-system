from .models import *
import django_filters

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['name']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['name']

class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['name']