from . models import *
from django.forms import ModelForm

class CreateTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class CreateStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CreateStaff(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'