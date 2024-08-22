from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField( max_length=100,null=False)

    def __str__(self):
        return self.name
    

class Staff(models.Model):
    ROLE_CHOICES = [
        ('Worker','Worker'),
        ('Chef','Chef'),
        ('Security','Security'),
        ('Cleaner','Cleaner'),
        ]
    name = models.CharField(max_length=100,null=False)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"{self.name} ({self.role})"


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    contact_number = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.subject.name})"
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    student_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.name} - Grade ({self.grade}) -Teacher ({self.student_teacher.name})"


class SchoolClass(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True )
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,blank=True)

    def __str__(self) -> str:
        return f"{self.name} -Teacher ({self.teacher.name}) -Students ({self.students.name})"