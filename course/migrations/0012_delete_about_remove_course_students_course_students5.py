# Generated by Django 4.1.4 on 2023-04-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_course_students_course_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='students5',
            field=models.ManyToManyField(null=True, related_name='course_students', to='course.student'),
        ),
    ]
