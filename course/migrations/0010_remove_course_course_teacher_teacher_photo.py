# Generated by Django 4.1.6 on 2023-04-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_course_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
