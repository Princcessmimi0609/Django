# Generated by Django 5.1.2 on 2024-10-14 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_attendance_attendence_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendence_id',
            new_name='attendence_number',
        ),
    ]
