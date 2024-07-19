from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class Course(models.Model):
    image = models.ImageField()
    slug = models.SlugField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    # teachers = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='course_teachers', null=True)
    students = models.ManyToManyField('Student', related_name='course_students') #, null=True

    # course_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} (+{self.last_name}) (+{self.phone_number})"


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    text = models.TextField()
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.first_name


# class GGroup(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.course


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text
