# Generated by Django 4.1.4 on 2023-04-19 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_remove_course_course_teacher_teacher_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(null=True, related_name='course_students', to='course.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_teachers', to='course.teacher'),
        ),
    ]
