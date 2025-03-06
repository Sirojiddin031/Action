# Generated by Django 5.1.6 on 2025-03-05 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_attendance', '0001_initial'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app_attendance.attendancelevel'),
        ),
    ]
