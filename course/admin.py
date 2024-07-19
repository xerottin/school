from django.contrib import admin

# Register your models here.
from course.models import Course, Review, Teacher, Student

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Teacher)
admin.site.register(Student)
