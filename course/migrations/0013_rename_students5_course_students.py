# Generated by Django 4.1.4 on 2023-04-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_delete_about_remove_course_students_course_students5'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='students5',
            new_name='students',
        ),
    ]
