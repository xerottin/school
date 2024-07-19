# Generated by Django 4.1.6 on 2023-04-17 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='client_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='client_number',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]